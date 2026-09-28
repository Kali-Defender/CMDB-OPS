"""
公共依赖模块。

职责：
1. get_db：为接口注入数据库会话
2. get_current_user：解析 JWT，获取当前登录用户（鉴权）
"""
from app.core.database import SessionLocal
# 导入会话工厂

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
# 创建会话，最后自动关闭
