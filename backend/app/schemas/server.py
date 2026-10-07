"""
服务器相关数据结构（Pydantic）。

- ServerCreate：新增服务器入参
- ServerUpdate：修改服务器入参
- ServerOut：返回给前端的服务器信息
"""
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional
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

class ServerCreate(BaseModel):
    name: str
    ip: str
    port: int = 22
    username: str
    password: str
    type: str = ""
    env: str = ""
    owner: str = ""
    status: str = "在线"
    remark: str = ""

class ServerUpdate(BaseModel):
    name: str
    ip: str
    port: int = 22
    username: str
    password: Optional[str] = None   # ← 关键：None = 不改密码
    type: str = ""
    env: str = ""
    owner: str = ""
    status: str = "在线"
    remark: str = ""