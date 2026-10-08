"""
执行记录相关数据结构（Pydantic）。

- RecordOut：返回给前端的执行记录
"""
from pydantic import BaseModel

class ExecuteRequest(BaseModel):
       server_ids: list[int]   # 要执行命令的服务器 id 列表
       command: str            # 要执行的命令

class ExecuteResult(BaseModel):
       server_id: int
       server_name: str
       ip: str
       success: bool
       output: str