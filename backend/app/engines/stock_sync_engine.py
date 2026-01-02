import sys
import os
import requests
from bs4 import BeautifulSoup
import datetime
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from pypinyin import pinyin, Style
import akshare as ak
import ast

from app.db.session import db
from app.models.base_data import BaseStockInfo
from loguru import logger

# 配置
LIST_URL = "http://www.haiguitouzi.com/doc/intro_stock_list.php"
MAX_WORKERS = 10  # 并发数量

class StockSyncEngine:
    FORCE_UPDATE_CONFIG_KEY = 'STOCK_SYNC_FORCE_UPDATE'
    ENABLE_UPDATE_CONFIG_KEY = 'STOCK_SYNC_ENABLE'
    # 默认调度间隔：每天 (秒)
    # 虽然是 1 天，但 run() 内部有预检查，所以可以设置得更短（例如 4 小时）以确保及时性
    # 这里设置为 12 小时检查一次
    SCHEDULE_INTERVAL = 43200 

    def __init__(self):
        self.session = requests.Session()
        # 模拟浏览器 User-Agent
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        })
        self.db_lock = Lock()

    def get_market_suffix(self, code):
        """根据股票代码推断市场后缀"""
        if code.startswith('6'):
            return 'SH'
        elif code.startswith('0') or code.startswith('3'):
            return 'SZ'
        elif code.startswith('8') or code.startswith('4'):
            return 'BJ'
        return 'SZ'

    def parse_date(self, date_str):
        """解析 'YYYYMMDD' 为日期对象"""
        if not date_str or not date_str.strip():
            return None
        try:
            return datetime.datetime.strptime(date_str.strip(), "%Y%m%d").date()
        except ValueError:
            return None
    
    def get_cnspell(self, name):
        """获取中文名称的拼音首字母"""
        if not name:
            return None
        try:
            # 剔除 * 号 (如 *ST)
            clean_name = name.replace('*', '')
            
            # NORMAL 模式下获取首字母需要配合 first_letter 风格? 
            # 实际上 pypinyin 的 FIRST_LETTER 风格可以直接获取首字母
            pinyins = pinyin(clean_name, style=Style.FIRST_LETTER)
            # pinyins 是一个列表的列表 [['p'], ['y']]
            return "".join([p[0] for p in pinyins if p]).lower()
        except Exception:
            return None

    def fetch_stock_list(self):
        """爬取完整股票列表"""
        logger.info(f"🔍 正在获取股票列表: {LIST_URL}")
        try:
            response = self.session.get(LIST_URL, timeout=30)
            response.encoding = 'utf-8'
            if response.status_code != 200:
                logger.error(f"❌ 获取列表失败: {response.status_code}")
                return []

            soup = BeautifulSoup(response.text, 'html.parser')
            tables = soup.find_all('table')
            target_table = None
            for table in tables:
                text = table.get_text()
                if "代码" in text and "名称" in text:
                    target_table = table
                    break
            
            if not target_table:
                logger.warning("⚠️ 未找到股票列表表格")
                return []

            rows = target_table.find_all('tr')
            logger.info(f"✔ 找到表格，共 {len(rows)} 行")
            
            stocks_to_upsert = []
            
            for row in rows:
                cols = row.find_all(['td', 'th'])
                for col in cols:
                    text = col.get_text(strip=True)
                    # 格式: 000001平安银行
                    if len(text) < 7: continue
                    
                    code = text[:6]
                    if not code.isdigit(): continue
                        
                    name = text[6:].strip()
                    if not name: continue
                    
                    suffix = self.get_market_suffix(code)
                    ts_code = f"{code}.{suffix}"
                    
                    # 生成拼音首字母
                    cnspell = self.get_cnspell(name)
                    
                    stocks_to_upsert.append({
                        "ts_code": ts_code,
                        "symbol": code,
                        "name": name,
                        "market": suffix,
                        "cnspell": cnspell
                    })
            
            return stocks_to_upsert

        except Exception as e:
            logger.error(f"❌ 获取列表时发生错误: {e}")
            return []

    def save_stock_list(self, stocks_data):
        """批量保存股票列表到数据库"""
        
        if not stocks_data:
            return
        
        logger.info(f"💾 正在保存/更新 {len(stocks_data)} 条股票基础信息...")
        count = 0
        with db.atomic():
            for item in stocks_data:
                try:
                    # 使用 Upsert 插入或更新
                    # 注意: list_date 不在此处更新，因为它来自详情页
                    # last_data 也不在此处更新，除非我们认为列表获取也算一次更新
                    BaseStockInfo.insert(
                        ts_code=item['ts_code'],
                        symbol=item['symbol'],
                        name=item['name'],
                        market=item['market'],
                        cnspell=item['cnspell']
                    ).on_conflict(
                        preserve=[BaseStockInfo.name, BaseStockInfo.market, BaseStockInfo.cnspell],
                        # 仅更新基础信息，不覆盖日期
                    ).execute()
                    count += 1
                except Exception as e:
                    logger.error(f"❌ 保存 {item['ts_code']} 失败: {e}")
        logger.success(f"✔ 列表保存完成")

    def fetch_single_detail(self, stock_id, ts_code, symbol, name):
        """获取单个股票详情的工作函数 (使用 Akshare)"""
        # 构造 akshare 需要的 symbol (如 SZ000001)
        ak_symbol = symbol
        try:
            market = ts_code.split('.')[-1]
            ak_symbol = f"{market}{symbol}"
        except:
            pass

        result = {
            "id": stock_id,
            "ts_code": ts_code,
            "success": False,
            "data": {},
            "error": None
        }
        
        try:
            # 随机延迟，避免被封 (虽然 API 可能不需要，但作为礼貌)
            time.sleep(random.uniform(0.1, 0.5))
            
            # 使用 akshare 获取数据
            # 注意: stock_individual_basic_info_xq 返回的是 DataFrame
            df = ak.stock_individual_basic_info_xq(symbol=ak_symbol)
            
            if df is None or df.empty:
                 result["error"] = "No data returned"
                 return result

            # 转换为字典: item -> value
            # 假设 df 有 item 和 value 列
            data_dict = df.set_index('item')['value'].to_dict()
            
            updates = {}
            
            # 映射字段
            # 1. 行业
            if 'affiliate_industry' in data_dict and data_dict['affiliate_industry']:
                ind_val = data_dict['affiliate_industry']
                # 可能是 dict 或 string representation
                if isinstance(ind_val, dict):
                     updates['industry'] = ind_val.get('ind_name')
                elif isinstance(ind_val, str):
                    try:
                        # 尝试 eval 安全解析，或者简单提取
                        if ind_val.startswith('{'):
                             ind_dict = ast.literal_eval(ind_val)
                             updates['industry'] = ind_dict.get('ind_name')
                        else:
                             updates['industry'] = ind_val
                    except:
                        updates['industry'] = ind_val # Fallback

            # 2. 地区
            if 'provincial_name' in data_dict and data_dict['provincial_name']:
                updates['area'] = data_dict['provincial_name']

            # 3. 上市时间
            if 'listed_date' in data_dict and data_dict['listed_date']:
                try:
                    ts = int(data_dict['listed_date'])
                    # 毫秒 -> date
                    d = datetime.date.fromtimestamp(ts / 1000)
                    updates['list_date'] = d
                except:
                    pass

            # 4. 实控人 (act_name)
            if 'actual_controller' in data_dict and data_dict['actual_controller']:
                 updates['act_name'] = data_dict['actual_controller']
            
            # 5. 企业类型 (act_ent_type)
            if 'classi_name' in data_dict and data_dict['classi_name']:
                 updates['act_ent_type'] = data_dict['classi_name']

            # 始终将 last_data 更新为今天
            updates['last_data'] = datetime.date.today()
            
            result["data"] = updates
            result["success"] = True
            
        except Exception as e:
            result["error"] = str(e)
            
        return result

    def update_details_concurrently(self, force_update=False):
        """并发获取股票详情"""
        
        if force_update:
            logger.info("🔥 强制更新模式: 将更新所有股票详情")

        today = datetime.date.today()
        
        # 选择需要更新的股票:
        query = BaseStockInfo.select()
        
        if not force_update:
            # 逻辑: 只要不是今天更新的，都需要更新
            # 即: last_data IS NULL OR last_data < today
            query = query.where(
                (BaseStockInfo.last_data.is_null(True)) | 
                (BaseStockInfo.last_data < today)
            )
        
        stocks = list(query)
        total = len(stocks)
        logger.info(f"📊 共找到 {total} 条需要更新详情的股票")
        
        if total == 0:
            logger.info("✨ 没有需要更新的股票")
            return

        success_count = 0
        failed_count = 0
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            # 映射 future 到 stock 对象以便记录日志
            future_to_stock = {
                executor.submit(
                    self.fetch_single_detail, 
                    stock.id, stock.ts_code, stock.symbol, stock.name
                ): stock for stock in stocks
            }
            
            for i, future in enumerate(as_completed(future_to_stock)):
                stock = future_to_stock[future]
                try:
                    res = future.result()
                    if res["success"]:
                        updates = res["data"]
                        if updates:
                            # 在主线程更新数据库 (Peewee 线程安全建议)
                            q = BaseStockInfo.update(updates).where(BaseStockInfo.id == res["id"])
                            q.execute()
                            success_count += 1
                            if i % 50 == 0:
                                logger.info(f"⏳ 进度: {i+1}/{total} - 已更新: {stock.name}")
                    else:
                        failed_count += 1
                        logger.warning(f"⚠️ 更新失败 {stock.ts_code}: {res['error']}")
                except Exception as e:
                    failed_count += 1
                    logger.error(f"❌ 处理结果异常 {stock.ts_code}: {e}")

        logger.success(f"✔ 详情更新完成: 成功 {success_count}, 失败 {failed_count}")

    def run(self, force_update=False):
        logger.info("🚀 启动股票基础数据同步引擎...")
        
        if db.is_closed():
            db.connect()
            
        try:
            # 0. 预检查：判断是否需要执行更新
            if force_update:
                logger.info("⚡ 检测到强制更新配置已开启 (由调用方传入)")

            if not force_update:
                # 检查是否有数据
                if not BaseStockInfo.select().exists():
                    logger.info("🆕 数据库为空，准备进行首次同步")
                else:
                    # 检查是否有过期数据
                    today = datetime.date.today()
                    has_outdated = BaseStockInfo.select().where(
                        (BaseStockInfo.last_data.is_null(True)) | 
                        (BaseStockInfo.last_data < today)
                    ).exists()
                    
                    if not has_outdated:
                        logger.info("✨ 所有股票基础数据已最新，跳过本次同步")
                        return

            # 阶段 1: 同步列表 (包含拼音)
            logger.info(">>> 1️⃣ 阶段1: 同步股票列表")
            stocks_list = self.fetch_stock_list()
            self.save_stock_list(stocks_list)
            
            # 阶段 2: 同步详情
            logger.info(">>> 2️⃣ 阶段2: 同步股票详情 (分布式/并发模式)")
            self.update_details_concurrently(force_update=force_update)
            
        finally:
            if not db.is_closed():
                db.close()
        logger.info("🏁 同步引擎任务结束")

if __name__ == "__main__":
    # 命令行入口支持
    engine = StockSyncEngine()
    engine.run()
