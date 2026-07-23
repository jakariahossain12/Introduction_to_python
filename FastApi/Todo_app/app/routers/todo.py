from sqlalchemy.orm import Session
from fastapi import APIRouter,HTTPException,Depends,status
from fastapi.responses import JSONResponse
from typing import Annotated
from app.auth.jwt_token import get_current_user

from database import db_dependency

from app.schemas.todo import CreateTodo,UpdateTodo
from app.crud.todo import create_todo,update_todo,get_all_todo,delete_todo



router = APIRouter(tags=["Todos"])

user_dependency = Annotated[dict,Depends(get_current_user)]

@router.get("/todos")
def getAll(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='failed Authentication')  
    return get_all_todo(db,owner_id=user.get('id'))


@router.post("/create-todo")
def create_todo_for_user(user:user_dependency,todo:CreateTodo,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='failed Authentication')
    
    create_todo(db,todo,user_id=user.get('id'))
    return JSONResponse(status_code=201,content={'message':'todo create successfully'})



@router.put("/update/{todo_id}")
def update_todo_for_user(user:user_dependency,upTodo:UpdateTodo,db:db_dependency,todo_id:int):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='failed Authentication')
    
    update_todo(db,todo_id,upTodo,owner_id=user.get('id'))
    return JSONResponse(status_code=201,content={'message':'todo update successfully'})


@router.delete("/delete/{todo_id}")
def delete_todo_for_user(user:user_dependency,db:db_dependency,todo_id:int):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='failed Authentication')
        
    delete_todo(db,todo_id,owner_id=user.get('id'))
    return JSONResponse(status_code=200,content={'message':'todo delete successfully'})