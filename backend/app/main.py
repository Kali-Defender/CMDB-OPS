"""
后端启动入口。

职责：
1. 创建 FastAPI 应用实例
2. 注册各业务路由（auth / servers / execute / records / users）
3. 配置 CORS 跨域，供前端调用
4. 应用启动时初始化数据库表

启动方式：uvicorn app.main:app --reload
"""
# 调用fastapi库创建应用实例
from fastapi import FastAPI
# models 包：数据库模型（ORM），对应 MySQL 中的三张表。
from app import models  
# 导入数据库基础类和引擎
from app.core.database import Base, engine
# 导入 auth 路由
from app.api import auth,servers,execute,records

from fastapi.middleware.cors import CORSMiddleware
#给后端配置CORS跨域，允许前端访问
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # 允许前端访问的域名
    allow_credentials=True, # 允许携带登录凭证
    allow_methods=["*"], # 允许所有 HTTP 方法
    allow_headers=["*"],# 允许所有请求头
)
# 注册 auth 路由，前缀为 /api
app.include_router(auth.router, prefix="/api")
app.include_router(servers.router, prefix="/api")
app.include_router(execute.router, prefix="/api")
app.include_router(records.router, prefix="/api")
@app.get("/")
async def root():
    return {"message": "Hello World"}

Base.metadata.create_all(bind=engine)