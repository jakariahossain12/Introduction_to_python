from fastapi import FastAPI

import models

from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

from routers import router

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the movie App API!"}
