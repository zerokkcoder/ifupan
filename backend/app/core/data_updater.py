import threading
import time
from loguru import logger
from app.db.session import db
from app.models.base_data import DataDictionary
from app.engines.stock_sync_engine import StockSyncEngine

class DataUpdater:
    """
    数据增量更新模块
    负责后台定期检查并更新数据
    支持多个更新引擎
    """
    def __init__(self):
        self._stop_event = threading.Event()
        self._thread = None
        # 注册更新引擎类
        self._engine_classes = [
            StockSyncEngine,
            # 后续在此处添加更多引擎
        ]

    def start(self):
        """启动后台更新线程"""
        if self._thread is not None and self._thread.is_alive():
            logger.warning("⚠️ 数据增量更新模块已在运行")
            return
        
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_loop, daemon=True, name="DataUpdaterThread")
        self._thread.start()
        logger.info("🚀 启动数据增量更新模块")

    def stop(self):
        """停止后台更新线程"""
        if self._thread:
            logger.info("🛑 正在停止数据增量更新模块...")
            self._stop_event.set()
            self._thread.join(timeout=5)
            logger.info("🏁 数据增量更新模块已停止")

    def _run_loop(self):
        """更新循环"""
        logger.info("⏳ 数据增量更新线程已启动，等待应用初始化...")
        # 初始等待，确保数据库和其他服务已完全启动
        time.sleep(10)
        
        while not self._stop_event.is_set():
            logger.info("⏱️ >>> 开始执行定期数据增量更新检查")
            
            for EngineClass in self._engine_classes:
                if self._stop_event.is_set():
                    break
                try:
                    engine_name = EngineClass.__name__
                    logger.info(f"🚀 正在运行更新引擎: {engine_name}")
                    
                    # 实例化
                    engine = EngineClass()
                    
                    # 检查是否有强制更新配置
                    force_update = False
                    config_key = getattr(EngineClass, 'FORCE_UPDATE_CONFIG_KEY', None)
                    if config_key:
                        # 临时连接数据库读取配置
                        if db.is_closed():
                            db.connect(reuse_if_open=True)
                        try:
                            config = DataDictionary.get_or_none(DataDictionary.dict_key == config_key)
                            if config and config.dict_value == '1':
                                force_update = True
                                logger.info(f"⚡ [DataUpdater] 引擎 {engine_name} 强制更新已开启")
                        except Exception as cfg_err:
                            logger.error(f"❌ 读取引擎配置失败: {cfg_err}")
                        finally:
                            if not db.is_closed():
                                db.close()

                    # 运行引擎 (传递 force_update 参数)
                    engine.run(force_update=force_update)
                    
                except Exception as e:
                    logger.error(f"❌ 引擎 {engine_name} 执行出错: {e}")
            
            logger.info("✔ <<< 本轮数据增量更新检查完成")
            
            # 休眠循环，支持响应停止信号
            # 默认每 1 小时检查一次
            check_interval_seconds = 3600 
            for _ in range(check_interval_seconds // 5): 
                if self._stop_event.is_set():
                    break
                time.sleep(5)

# 全局单例
data_updater = DataUpdater()
