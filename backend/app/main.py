from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from app.core.config import settings
from app.api.v1.api import api_router
from app.core.logger import setup_logging
from app.db.session import db
from app.models import (
    BaseStockInfo, DataDictionary, DbMetadata,
    AntMonitorStock, AntMonitorTag, AntMonitorSystem, AntMonitorSystemRecord,
    StrategyClassInfo, AntStrategyFound, StrategyBindSetting,
    AntRiskAssessment, AntRiskAssessmentItem, AntRiskSystemAssessment,
    AntMonitorDay, KLineData,
    StockValuation, StockValuationResult,
    AntMonitorDiary, AntMonitorPlate, AntMonitorPlateLink,
    MonitorAiConfig, MonitorAiAgent,
    AntNewsSearchRecord, AutomationOperationLog
)

def create_tables():
    """初始化数据库表结构"""
    with db:
        db.create_tables([
            BaseStockInfo, DataDictionary, DbMetadata,
            AntMonitorStock, AntMonitorTag, AntMonitorSystem, AntMonitorSystemRecord,
            StrategyClassInfo, AntStrategyFound, StrategyBindSetting,
            AntRiskAssessment, AntRiskAssessmentItem, AntRiskSystemAssessment,
            AntMonitorDay, KLineData,
            StockValuation, StockValuationResult,
            AntMonitorDiary, AntMonitorPlate, AntMonitorPlateLink,
            MonitorAiConfig, MonitorAiAgent,
            AntNewsSearchRecord, AutomationOperationLog
        ])
    logger.success("✔ 数据库表已检查/创建")

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    
    # 连接数据库
    try:
        db.connect()
        logger.success("✔  数据库连接成功")
        create_tables()
    except Exception as e:
        logger.error(f"❌ 数据库连接失败: {e}")
        
    logger.success("✔ 应用启动完成")
    yield
    
    # 关闭数据库连接
    if not db.is_closed():
        db.close()
        logger.success("✔ 数据库连接已断开")
    logger.success("✔ 应用已关闭")

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    logger.info("✔ 根接口访问成功")
    return {"message": "Welcome to Stock Fupan API"}
