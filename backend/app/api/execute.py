"""
批量执行命令接口路由。

- POST /api/execute：对勾选的服务器批量 SSH 执行命令
对应文档「接口清单」第 6 条。
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.server import Server
from app.models.record import Record
from app.schemas.record import ExecuteRequest, ExecuteResult
from app.services.ssh_service import execute_ssh

router = APIRouter()

@router.post("/execute", response_model=list[ExecuteResult])
def execute_command(data: ExecuteRequest, db: Session = Depends(get_db),current_user=Depends(get_current_user)):
       # 1. 查出勾选的服务器
       servers = db.query(Server).filter(Server.id.in_(data.server_ids)).all()

       # 2. 逐台执行，收集结果
       results = []
       for server in servers:
           r = execute_ssh(server.ip, server.port, server.username, server.password,data.command)
           results.append(ExecuteResult(
               server_id=server.id,
               server_name=server.name,
               ip=server.ip,
               success=r["success"],
               output=r["output"],
           ))

       # 3. 存执行记录（审计）
       success_count = sum(1 for r in results if r.success)
       record = Record(
           executor=current_user.username,
           servers=",".join(s.name for s in servers),
           command=data.command,
           result=f"{success_count} 台成功 / {len(results) - success_count} 台失败",
           status="成功" if success_count == len(results) else "部分失败",
       )
       db.add(record)
       db.commit()

       return results