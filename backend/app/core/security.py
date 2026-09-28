"""
安全模块。

职责：
1. 密码哈希：明文密码加密存储、校验
2. JWT：生成登录令牌、解析校验令牌
"""
import bcrypt
# 处理明文转哈希和哈希加盐
from jose import jwt
# 处理用户登录令牌
from datetime import datetime, timedelta, timezone
# 处理令牌的过期时间
from app.core.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
# 引入 JWT 密钥和令牌过期时间

def hash_password(password:str)->str:
    pwd=password.encode("utf-8")
    # 将字符串密码明文转按utf-8的编码模式编码
    hashed=bcrypt.hashpw(pwd,bcrypt.gensalt())
    # 将密码明文转哈希并加盐
    return hashed.decode("utf-8")
    # 将哈希转按utf-8的编码模式解码

def verify_password(password:str,hashed:str)->bool:
    return bcrypt.checkpw(password.encode("utf-8"),hashed.encode("utf-8"))
    # 将密码明文和哈希对比检查

def create_access_token(data:dict)->str:
    to_encode=data.copy()
    # 复制一份，别改原数据
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # 计算过期时间点
    to_encode["exp"]=expire
    # 将过期时间塞进数据，给数据设置过期时间
    return jwt.encode(to_encode,SECRET_KEY,algorithm="HS256")
    # 利用签名封装令牌

def decode_access_token(token:str)->dict:
    return jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
    # 验证签名并取回数据