"""
用户表模型（users）。

字段：用户名、密码（加密）、姓名、角色、状态、创建时间
对应文档「数据库表设计 - 用户表」。
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, comment="主键ID")
    username = Column(String(50), unique=True, nullable=False, index=True, comment="用户名")
    password = Column(String(255), nullable=False, comment="密码")
    name = Column(String(50), comment="姓名")
    role = Column(String(20), default="普通运维", comment="角色")
    status = Column(String(20), default="启用", comment="状态")
    created_at = Column(DateTime, server_default=func.now(), comment="创建时间")
