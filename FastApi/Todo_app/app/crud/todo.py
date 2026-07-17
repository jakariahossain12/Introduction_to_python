from sqlalchemy.orm import Session
import app.models as models
from fastapi import HTTPException

from app.schemas.todo import CreateTodo,UpdateTodo





def create_todo(db:Session,todo:CreateTodo, user_id:int):
    new_todo = models.todo.Todos(**todo.model_dump(),owner_id=user_id)
    db.add(new_todo)
    db.commit()


def get_all_todo(db:Session):
    return db.query(models.todo.Todos).all()




def update_todo(db:Session,todo_id : int, updateTodo:UpdateTodo):
    todo = db.query(models.todo.Todos).filter(models.todo.Todos.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="todo not found")
    
    update_data = updateTodo.model_dump(exclude_unset=True)

    for key,value in update_data.items():
        setattr(todo,key,value)
    
    db.commit()



def delete_todo(db:Session,todo_id : int):
    todo = db.query(models.todo.Todos).filter(models.todo.Todos.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="todo not found")

    db.query(models.todo.Todos).filter(models.todo.Todos.id == todo_id).delete()
    db.commit()