"""
执行记录接口路由。

- GET /api/records：获取执行记录列表（支持按执行人/服务器/时间筛选）
对应文档「接口清单」第 7 条。
"""
from fastapi import APIRouter, Depends                                                                                                                                            
from sqlalchemy.orm import Session                                                                                                                                                
                                                                                                                                                                                     
from app.api.deps import get_db, get_current_user                                                                                                                                 
from app.models.record import Record                                                                                                                                              
from app.schemas.record import RecordOut                                                                                                                                          
                                                                                                                                                                                     
router = APIRouter()                                                                                                                                                              
                                                                                                                                                                                     
@router.get("/records", response_model=list[RecordOut])                                                                                                                           
def list_records(db: Session = Depends(get_db), current_user=Depends(get_current_user)):                                                                                          
       records = db.query(Record).all()                                                                                                                                              
       return records