from apscheduler.schedulers.background import BackgroundScheduler
from app.core.database import SessionLocal
from app.models.server import Server
from app.models.record import Record
from app.core.security import decrypt_password
from app.services.ssh_service import execute_ssh
def inspect_task():
       db = SessionLocal()
       try:
           servers = db.query(Server).all()
           if not servers:              # 没有服务器就别写空记录
               return

           results = []
           for server in servers:
               r = execute_ssh(server.ip, server.port, server.username,
                               decrypt_password(server.password), "df -h")
               results.append(r)        # ← 收集结果（补这里）

           success_count = sum(1 for r in results if r["success"])
           record = Record(             # ← 写执行记录（补这里）
               executor="系统巡检",       # 区别于手动执行
               servers=",".join(s.name for s in servers),
               command="df -h",
               result=f"{success_count} 台成功 / {len(results) - success_count} 台失败",
               status="成功" if success_count == len(results) else "部分失败",
           )
           db.add(record)
           db.commit()
       finally:
           db.close()

scheduler = BackgroundScheduler()

def start_scheduler():
       scheduler.add_job(inspect_task, 'interval', minutes=60)   # 每 60 分钟
       scheduler.start()