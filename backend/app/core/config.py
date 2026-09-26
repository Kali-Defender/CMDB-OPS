"""
配置模块。

职责：
1. 从 .env 读取数据库连接串、JWT 密钥、令牌过期时间等配置
2. 提供全局可用的配置变量
"""
import os
from dotenv import load_dotenv

# 读取.env文件里的键值对
load_dotenv()

# os.getenv(key，默认值) 函数用于获取指定环境变量的值。如果环境变量不存在，返回 None。
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",5000))

# 环境变量找不到时的处理逻辑
if not DATABASE_URL:
    raise ValueError("环境变量缺失: DATABASE_URL 未配置")
if not SECRET_KEY:
    raise ValueError("环境变量缺失: SECRET_KEY 未配置")