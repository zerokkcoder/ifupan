from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import api_router
from app.api.root import root_router
from app.core.lifespan import lifespan
from app.core.middleware import setup_middlewares

def create_application() -> FastAPI:
    """
    创建并配置 FastAPI 应用实例
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        lifespan=lifespan
    )

    setup_middlewares(app)

    app.include_router(api_router, prefix=settings.API_V1_STR)
    app.include_router(root_router)
    
    return app
