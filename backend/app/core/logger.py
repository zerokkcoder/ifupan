import logging
import sys
from pathlib import Path
from loguru import logger

class InterceptHandler(logging.Handler):
    """
    将标准 logging 日志拦截并转发给 loguru
    """
    def emit(self, record):
        # 获取对应的 Loguru level
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # 查找调用者的 frame
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )

def setup_logging():
    """
    配置日志系统
    """
    # 拦截标准 logging
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(logging.INFO)

    # 接管 uvicorn 和 fastapi 的日志
    for name in logging.root.manager.loggerDict.keys():
        if name.startswith("uvicorn") or name.startswith("fastapi"):
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True
 
    # 配置 loguru
    logger.remove() # 移除默认配置
    
    # 1. 控制台输出
    logger.add(
        sys.stderr,
        level="INFO",
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )
    
    # 2. 文件输出 (按天轮转，保留 30 天)
    # 确保日志目录存在
    log_path = Path("logs")
    log_path.mkdir(exist_ok=True)
    
    logger.add(
        str(log_path / "app_{time:YYYY-MM-DD}.log"),
        rotation="00:00", # 每天午夜轮转
        retention="30 days", # 保留30天
        level="INFO",
        encoding="utf-8",
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
        enqueue=True # 异步写入
    )
    
    logger.success("✔ 日志系统初始化成功")
    return logger
