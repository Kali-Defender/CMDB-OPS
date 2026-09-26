"""
数据库模块。

职责：
1. 创建 SQLAlchemy 引擎与会话工厂
2. 定义 Base 基类，供各模型继承
3. 提供 engine 与 Base，供建表使用
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import app.core.config

# 创建 SQLAlchemy 引擎
engine=create_engine(
    app.core.config.DATABASE_URL, 
    pool_pre_ping=True
)

# 创建会话工厂
SessionLocal=sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

# 定义 Base 基类
Base=declarative_base()
