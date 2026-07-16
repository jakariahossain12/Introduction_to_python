from fastapi import FastAPI

from app.routers.books import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def server_running():
    return {'message':"server running"}