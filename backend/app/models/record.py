"""
执行记录表模型（records）。

字段：执行人、服务器、命令、结果、状态、执行时间
对应文档「数据库表设计 - 执行记录表」。
"""
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.core.database import Base

class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, comment="主键ID")
    executor = Column(String(50), comment="执行人")
    servers = Column(String(500), comment="执行的服务器")
    command = Column(String(500), comment="执行的命令")
    result = Column(Text, comment="执行结果")
    status = Column(String(20), comment="状态")
    executed_at = Column(DateTime, server_default=func.now(), comment="执行时间")

