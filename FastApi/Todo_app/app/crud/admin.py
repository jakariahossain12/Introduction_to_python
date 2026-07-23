from sqlalchemy.orm import Session
import app.models as models
from fastapi import HTTPException

from app.schemas.todo import CreateTodo,UpdateTodo


def get_all_todo(db:Session):
    return db.query(models.todo.Todos).all()
