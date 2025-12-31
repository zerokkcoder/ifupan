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
    logger.info("Database tables checked/created")

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    
    # 连接数据库
    try:
        db.connect()
        logger.info("Database connected")
        create_tables()
    except Exception as e:
        logger.error(f"Database connection error: {e}")
        
    logger.info("Application startup complete")
    yield
    
    # 关闭数据库连接
    if not db.is_closed():
        db.close()
        logger.info("Database disconnected")
    logger.info("Application shutdown")

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
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to Stock Fupan API"}
