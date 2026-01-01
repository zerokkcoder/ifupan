from contextlib import asynccontextmanager
from fastapi import FastAPI
from loguru import logger
from app.core.logger import setup_logging
from app.db.session import db
from app.db.init_db import init_db
from app.core.data_updater import data_updater

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    应用生命周期管理
    负责初始化日志、数据库连接以及应用关闭时的清理工作
    """
    setup_logging()
    
    # 连接数据库
    try:
        db.connect()
        logger.success("✔ 数据库连接成功")
        init_db()
    except Exception as e:
        logger.error(f"❌ 数据库连接失败: {e}")
        
    # 启动数据增量更新模块
    data_updater.start()

    logger.success("✔ 应用启动完成")
    yield
    
    # 停止数据增量更新模块
    data_updater.stop()
    
    # 关闭数据库连接
    if not db.is_closed():
        db.close()
        logger.success("✔ 数据库连接已断开")
    logger.success("✔ 应用已关闭")
