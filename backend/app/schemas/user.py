"""
用户相关数据结构（Pydantic）。

- UserCreate：创建用户（初始化管理员）
- UserOut：返回给前端的用户信息
"""
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class UserOut(BaseModel):
       model_config = ConfigDict(from_attributes=True)

       id: int
       username: str
       name: str
       role: str
       status: str
       created_at: datetime
class UserCreate(BaseModel):
       username: str
       password: str                      # 明文，后端哈希后存
       name: str = ""
       role: str = "普通运维"
       status: str = "启用"