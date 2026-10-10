from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.server import Server
from app.models.record import Record
from app.core.security import decrypt_password
from app.services.sftp_service import upload_file

router = APIRouter()

@router.post("/deploy")
async def deploy(
       file: UploadFile = File(...),              # 上传的文件
       server_ids: str = Form(...),               # 目标服务器 id（逗号分隔，如 "1,2,3"）
       remote_path: str = Form(...),              # 远程路径，如 /tmp/nginx.conf
       db: Session = Depends(get_db),
       current_user=Depends(get_current_user),
   ):
       file_data = await file.read()              # 读文件内容（bytes）
       ids = [int(x) for x in server_ids.split(",")]
       servers = db.query(Server).filter(Server.id.in_(ids)).all()

       results = []
       for server in servers:
           r = upload_file(server.ip, server.port, server.username,
                           decrypt_password(server.password), file_data, remote_path)
           results.append({
               "server_id": server.id,
               "server_name": server.name,
               "success": r["success"],
               "output": r["output"],
           })

       # 写执行记录（审计）
       ok = sum(1 for r in results if r["success"])
       db.add(Record(
           executor=current_user.username,
           servers=",".join(s.name for s in servers),
           command=f"配置下发 → {remote_path}",
           result=f"{ok} 台成功 / {len(results) - ok} 台失败",
           status="成功" if ok == len(results) else "部分失败",
       ))
       db.commit()

       return results