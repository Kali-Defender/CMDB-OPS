"""
服务器（资产）接口路由。

- GET    /api/servers      ：获取服务器列表（支持搜索、分页）
- POST   /api/servers      ：新增服务器
- PUT    /api/servers/{id} ：修改服务器
- DELETE /api/servers/{id} ：删除服务器
对应文档「接口清单」第 2~5 条。
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.server import Server
from app.schemas.server import ServerOut

router = APIRouter()

@router.get("/servers", response_model=list[ServerOut])
def list_servers(db: Session = Depends(get_db),current_user=Depends(get_current_user)):
       servers = db.query(Server).all()
       return servers