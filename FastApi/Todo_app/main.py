from fastapi import FastAPI

import app.models as models
from database import engine

from app.routers import todo
from app.routers import user

app = FastAPI(title="todo api")
models.Base.metadata.create_all(bind=engine)
app.include_router(todo.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Todo App API!"}