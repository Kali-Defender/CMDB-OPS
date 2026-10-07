"""
服务器（资产）接口路由。

- GET    /api/servers      ：获取服务器列表（支持搜索、分页）
- POST   /api/servers      ：新增服务器
- PUT    /api/servers/{id} ：修改服务器
- DELETE /api/servers/{id} ：删除服务器
对应文档「接口清单」第 2~5 条。
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.core.security import hash_password
from app.models.server import Server
from app.schemas.server import ServerCreate, ServerUpdate, ServerOut

router = APIRouter()

@router.get("/servers", response_model=list[ServerOut])
def list_servers(db: Session = Depends(get_db),current_user=Depends(get_current_user)):
       servers = db.query(Server).all()
       return servers

@router.post("/servers", response_model=ServerOut)
def create_server(data: ServerCreate, db: Session = Depends(get_db),current_user=Depends(get_current_user)):
       # 1. 校验 IP 是否重复
       exists = db.query(Server).filter(Server.ip == data.ip).first()
       if exists:
           raise HTTPException(status_code=400, detail="该 IP 已存在")

       # 2. 创建服务器对象
       server = Server(
           name=data.name,
           ip=data.ip,
           port=data.port,
           username=data.username,
           password=hash_password(data.password),  
           type=data.type,
           env=data.env,
           owner=data.owner,
           status=data.status,
           remark=data.remark,
       )

       # 3. 保存到数据库
       db.add(server)
       db.commit()
       db.refresh(server)   
       return server

@router.put("/servers/{server_id}", response_model=ServerOut)
def update_server(server_id: int, data: ServerUpdate, db: Session = Depends(get_db),current_user=Depends(get_current_user)):
       # 1. 查找服务器
       server = db.query(Server).filter(Server.id == server_id).first()
       if server is None:
           raise HTTPException(status_code=404, detail="服务器不存在")

       # 2. 更新普通字段
       server.name = data.name
       server.ip = data.ip
       server.port = data.port
       server.username = data.username
       server.type = data.type
       server.env = data.env
       server.owner = data.owner
       server.status = data.status
       server.remark = data.remark

       # 3. 密码特殊处理：传了才改，没传保留原密码
       if data.password:  # 非空才改（None 和 "" 都跳过）
           server.password = hash_password(data.password)

       # 4. 保存
       db.commit()
       db.refresh(server)
       return server

@router.delete("/servers/{server_id}")
def delete_server(server_id: int, db: Session = Depends(get_db),current_user=Depends(get_current_user)):
       server = db.query(Server).filter(Server.id == server_id).first()
       if server is None:
           raise HTTPException(status_code=404, detail="服务器不存在")

       db.delete(server)
       db.commit()
       return {"message": "删除成功"}