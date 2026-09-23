"""
后端启动入口。

职责：
1. 创建 FastAPI 应用实例
2. 注册各业务路由（auth / servers / execute / records / users）
3. 配置 CORS 跨域，供前端调用
4. 应用启动时初始化数据库表

启动方式：uvicorn app.main:app --reload
"""
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
