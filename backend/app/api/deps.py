"""
公共依赖模块。

职责：
1. get_db：为接口注入数据库会话
2. get_current_user：解析 JWT，获取当前登录用户（鉴权）
"""
from app.core.database import SessionLocal
# 导入会话工厂
from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.models.user import User

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
# 创建会话，最后自动关闭

def get_current_user(authorization: str = Header(None), db: Session =
 Depends(get_db)):
       # 1. 检查是否带了 token（标准格式是 "Bearer <token>"）
       if not authorization or not authorization.startswith("Bearer "):
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="未登录")
       # 2. 去掉 "Bearer " 前缀，拿到纯 token
       token = authorization.split(" ")[1]
       # 3. 解码 token，取出用户名
       try:
           payload = decode_access_token(token)
       except Exception:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="令牌无效")
       username = payload.get("sub")
       if username is None:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="令牌无效")
       # 4. 查用户是否存在
       user = db.query(User).filter(User.username == username).first()
       if user is None:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="用户不存在")
       return user