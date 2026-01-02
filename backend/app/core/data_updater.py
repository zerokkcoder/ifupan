import threading
import time
from concurrent.futures import ThreadPoolExecutor
from loguru import logger
from app.db.session import db
from app.models.base_data import DataDictionary
from app.engines.stock_sync_engine import StockSyncEngine

class DataUpdater:
    """
    数据增量更新模块 (轻量级调度版)
    负责后台定期检查并更新数据
    支持多个更新引擎，支持自定义调度间隔，并发执行
    """
    def __init__(self):
        self._stop_event = threading.Event()
        self._thread = None
        # 使用线程池并发执行任务，避免单个引擎阻塞调度循环
        # max_workers 设置为 4，根据实际情况调整
        self._executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="DataUpdaterWorker")
        
        # 记录每个引擎的上一次运行时间
        self._engine_last_run = {}
        
        # 注册更新引擎类
        self._engine_classes = [
            StockSyncEngine,
            # 后续在此处添加更多引擎
        ]

    def start(self):
        """启动后台调度线程"""
        if self._thread is not None and self._thread.is_alive():
            logger.warning("⚠️ 数据增量更新模块已在运行")
            return
        
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._scheduler_loop, daemon=True, name="DataUpdaterScheduler")
        self._thread.start()
        logger.info("🚀 启动数据增量更新模块 (Lightweight Scheduler)")

    def stop(self):
        """停止后台更新线程"""
        if self._thread:
            logger.info("🛑 正在停止数据增量更新模块...")
            self._stop_event.set()
            self._thread.join(timeout=5)
            # 停止线程池
            self._executor.shutdown(wait=False)
            logger.info("🏁 数据增量更新模块已停止")

    def _run_engine_task(self, EngineClass):
        """执行单个引擎任务的包装函数"""
        engine_name = EngineClass.__name__
        try:
            logger.info(f"🚀 [DataUpdater] 启动任务: {engine_name}")
            
            # 检查配置 (启用开关 和 强制更新)
            enable_key = getattr(EngineClass, 'ENABLE_UPDATE_CONFIG_KEY', None)
            force_key = getattr(EngineClass, 'FORCE_UPDATE_CONFIG_KEY', None)
            
            is_enabled = True # 默认为启用
            force_update = False
            
            if enable_key or force_key:
                # 临时连接数据库读取配置
                if db.is_closed():
                    db.connect(reuse_if_open=True)
                try:
                    # 1. 检查启用开关
                    if enable_key:
                        config = DataDictionary.get_or_none(DataDictionary.dict_key == enable_key)
                        if config:
                            # 支持 0, false, off 为禁用
                            if config.dict_value.lower() in ['0', 'false', 'off']:
                                is_enabled = False
                                logger.info(f"🛑 [DataUpdater] 引擎 {engine_name} 已通过配置禁用 ({enable_key}=0)")
                    
                    # 2. 检查强制更新 (仅当启用时)
                    if is_enabled and force_key:
                        config = DataDictionary.get_or_none(DataDictionary.dict_key == force_key)
                        if config and config.dict_value == '1':
                            force_update = True
                            logger.info(f"⚡ [DataUpdater] 引擎 {engine_name} 强制更新已开启")
                            
                except Exception as cfg_err:
                    logger.error(f"❌ [DataUpdater] 读取引擎配置失败: {cfg_err}")
                finally:
                    if not db.is_closed():
                        db.close()
            
            if not is_enabled:
                return

            # 实例化
            engine = EngineClass()
            
            # 运行引擎 (传递 force_update 参数)
            engine.run(force_update=force_update)
            logger.success(f"✔ [DataUpdater] 任务完成: {engine_name}")
            
        except Exception as e:
            logger.error(f"❌ [DataUpdater] 引擎 {engine_name} 执行出错: {e}")

    def _scheduler_loop(self):
        """调度主循环"""
        logger.info("⏳ 数据调度器已启动，等待应用初始化...")
        # 初始等待
        time.sleep(10)
        
        while not self._stop_event.is_set():
            now = time.time()
            
            for EngineClass in self._engine_classes:
                if self._stop_event.is_set():
                    break
                
                # 获取引擎配置的间隔，默认为 1 小时 (3600秒)
                interval = getattr(EngineClass, 'SCHEDULE_INTERVAL', 3600)
                last_run = self._engine_last_run.get(EngineClass, 0)
                
                # 检查是否到达执行时间
                if now - last_run >= interval:
                    # 更新最后运行时间
                    self._engine_last_run[EngineClass] = now
                    
                    # 提交到线程池执行，不阻塞调度循环
                    self._executor.submit(self._run_engine_task, EngineClass)
            
            # 短暂休眠，提高响应速度
            # 10秒检查一次，支持分钟级任务
            for _ in range(10): 
                if self._stop_event.is_set():
                    break
                time.sleep(1)

# 全局单例
data_updater = DataUpdater()
