"""
登录令牌相关数据结构（Pydantic）。

- LoginRequest：登录入参（用户名、密码）
- Token：登录响应（access_token、token_type）
"""
from pydantic import BaseModel
# BaseModel 是 Pydantic 的基类，继承它，你的类就变成"数据模型"（和之前 SQLAlchemy 的Base 一个套路）。

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token:str
    token_type:str="bearer"