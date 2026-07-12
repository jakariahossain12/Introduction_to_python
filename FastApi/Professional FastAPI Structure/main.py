from fastapi import FastAPI

from app.routers.patient import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Server Running"}