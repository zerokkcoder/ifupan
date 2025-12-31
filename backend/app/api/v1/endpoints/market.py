from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def get_market_status():
    """
    获取市场概览状态（模拟数据）
    """
    return {
        "status": "Open",
        "index": 3000.50,
        "change": "+1.2%"
    }
