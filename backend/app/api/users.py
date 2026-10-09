"""
当前用户信息接口路由。

- GET /api/users/me：获取当前登录用户信息
对应文档「接口清单」第 8 条。
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserOut, UserCreate

router = APIRouter()

@router.get("/users/me", response_model=UserOut)
def get_me(current_user=Depends(get_current_user)):
       return current_user

@router.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
       if current_user.role != "管理员":
           raise HTTPException(status_code=403, detail="需要管理员权限")
       return db.query(User).all()

@router.post("/users", response_model=UserOut)
def create_user(data: UserCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
       if current_user.role != "管理员":
           raise HTTPException(status_code=403, detail="需要管理员权限")
       exists = db.query(User).filter(User.username == data.username).first()
       if exists:
           raise HTTPException(status_code=400, detail="用户名已存在")

       user = User(
           username=data.username,
           password=hash_password(data.password),   # ★ 用户密码用「哈希」
           name=data.name,
           role=data.role,
           status=data.status,
       )
       db.add(user)
       db.commit()
       db.refresh(user)
       return user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
       if current_user.role != "管理员":
           raise HTTPException(status_code=403, detail="需要管理员权限")
       user = db.query(User).filter(User.id == user_id).first()
       if user is None:
           raise HTTPException(status_code=404, detail="用户不存在")
       if user.id == current_user.id:
           raise HTTPException(status_code=400, detail="不能删除自己")
       db.delete(user)
       db.commit()
       return {"message": "删除成功"}