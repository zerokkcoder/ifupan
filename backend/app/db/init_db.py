from loguru import logger
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

def init_db():
    """
    初始化数据库表结构
    
    创建所有定义的数据模型对应的数据库表。
    如果表已存在，peewee 会自动跳过。
    """
    try:
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
    except Exception as e:
        logger.error(f"❌ 数据库表创建失败: {e}")
        raise e
