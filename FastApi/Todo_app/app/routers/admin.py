from sqlalchemy.orm import Session
from fastapi import APIRouter,HTTPException,Depends,status
from fastapi.responses import JSONResponse
from typing import Annotated
from app.auth.jwt_token import get_current_user

from database import db_dependency

from app.schemas.todo import CreateTodo,UpdateTodo
from app.crud.admin import get_all_todo



router = APIRouter(tags=["Admin"])

user_dependency = Annotated[dict,Depends(get_current_user)]

@router.get("/admin-todo-all")
def get_All_Todo(user: user_dependency, db: db_dependency):
    # 1. Check if user is authenticated
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Failed Authentication"
        )
    
    # 2. Check if user has admin privileges
    if user.get('role') != 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Forbidden: Admin access required"
        )
        
    return get_all_todo(db)



