from database import db_dependency

from app.schemas.user import UserCreate

from app.crud.user import user_create

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/user',tags=['Users'])

@router.post("/post")
def new_users(db:db_dependency,user:UserCreate):
    user_create(db,user)
    return JSONResponse(status_code=201,content={'message':'user create successfully'})