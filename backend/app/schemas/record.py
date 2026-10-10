"""
执行记录相关数据结构（Pydantic）。

- ExecuteRequest：批量执行命令的入参
- ExecuteResult：单台服务器的执行结果
- RecordOut：返回给前端的执行记录
"""
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ExecuteRequest(BaseModel):
    server_ids: list[int]   # 要执行命令的服务器 id 列表
    command: str            # 要执行的命令


class ExecuteResult(BaseModel):
    server_id: int
    server_name: str
    ip: str
    success: bool
    output: str


class RecordOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    executor: str
    servers: str
    command: str
    result: str
    status: str
    executed_at: datetime
