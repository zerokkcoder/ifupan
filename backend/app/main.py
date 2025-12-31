import uvicorn
from app.bootstrap.application import create_application

app = create_application()

if __name__ == "__main__":
    # 使用 uvicorn 启动应用
    # host="0.0.0.0" 允许外部访问
    # port=8000 指定端口
    # reload=True 开发模式下代码变动自动重启
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
