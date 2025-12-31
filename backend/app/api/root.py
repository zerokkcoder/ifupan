from fastapi import APIRouter
from loguru import logger

root_router = APIRouter()

@root_router.get("/")
def root():
    logger.info("✔ 根接口访问成功")
    return {"message": "Welcome to Stock Fupan API"}
