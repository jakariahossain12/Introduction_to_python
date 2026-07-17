from sqlalchemy.orm import Session
from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse

from database import db_dependency

from app.schemas.todo import CreateTodo,UpdateTodo
from app.crud.todo import create_todo,update_todo,get_all_todo,delete_todo

router = APIRouter(tags=["Todos"])

@router.get("/todos")
def getAll(db:db_dependency):
    return get_all_todo(db)


@router.post("/post")
def create_todo_for_user(todo:CreateTodo,db:db_dependency,owner_id:int):
    create_todo(db,todo,owner_id)
    return JSONResponse(status_code=201,content={'message':'todo create successfully'})

@router.put("/update/{todo_id}")
def update_todo_for_user(upTodo:UpdateTodo,db:db_dependency,todo_id):
    update_todo(db,todo_id,upTodo)
    return JSONResponse(status_code=201,content={'message':'todo update successfully'})

@router.delete("/delete/{todo_id}")
def delete_todo_for_user(db:db_dependency,todo_id:int):
    delete_todo(db,todo_id)
    return JSONResponse(status_code=200,content={'message':'todo delete successfully'})