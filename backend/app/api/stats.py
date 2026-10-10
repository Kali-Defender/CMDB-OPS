from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.server import Server
from app.models.record import Record
from app.models.user import User

router = APIRouter()



@router.get("/stats")
def get_stats(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
       return {
           "server_total": db.query(Server).count(),
           "server_online": db.query(Server).filter(Server.status == "在线").count(),
           "record_total": db.query(Record).count(),
           "user_total": db.query(User).count(),
       }
