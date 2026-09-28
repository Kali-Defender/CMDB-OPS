"""
登录接口路由。

- POST /api/login：验证用户名密码，返回 JWT 令牌
对应文档「接口清单」第 1 条。
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
# 导入会话
from app.core.security import verify_password, create_access_token
# 导入验证密码和生成令牌
from app.models.user import User
# 导入用户表
from app.schemas.token import LoginRequest, Token
# 导入请求和响应的格式

router = APIRouter()
# 创建路由分组

@router.post("/login",response_model=Token) 
# 请求方式为POST 请求路径为/login 响应格式为Token
def login(data:LoginRequest,db:Session = Depends(get_db)):
    # 参数为用户输入的账密数据和数据库会话
    user = db.query(User).filter(User.username == data.username).first()
    # 查用户是否存在，没有直接返回None
    if not user or not verify_password(data.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
        )
    # 综合判定账密是否正确
    token = create_access_token({"sub":user.username})
    # 封装令牌
    return Token(access_token=token,token_type="bearer")
    # 返回Token

