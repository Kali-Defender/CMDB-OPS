"""
服务器相关数据结构（Pydantic）。

- ServerCreate：新增服务器入参
- ServerUpdate：修改服务器入参
- ServerOut：返回给前端的服务器信息
"""
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ServerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)   # ← 自动转换的开关

    id: int
    name: str
    ip: str
    port: int
    username: str
    type: str
    env: str
    owner: str
    status: str
    remark: str
    created_at: datetime