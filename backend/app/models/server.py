"""
服务器表模型（servers）。

字段：名称、IP、端口、登录账号、密码/密钥（加密）、类型、环境、
负责人、状态、备注、创建时间
对应文档「数据库表设计 - 服务器表」。
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Server(Base):
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True, comment="主键ID")
    name = Column(String(100), nullable=False, comment="服务器名称")
    ip = Column(String(50), unique=True, nullable=False, index=True, comment="IP地址")
    port = Column(Integer, default=22, comment="SSH端口")
    username = Column(String(50), comment="用户名")
    password = Column(String(255), comment="密码")
    type = Column(String(20), comment="服务器类型")
    env = Column(String(20), comment="环境")
    owner = Column(String(50), comment="负责人")
    status = Column(String(20), default="在线", comment="状态")
    remark = Column(String(500), comment="备注")
    created_at = Column(DateTime, server_default=func.now(), comment="创建时间")
