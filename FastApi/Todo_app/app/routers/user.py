from database import db_dependency

from app.schemas.user import UserCreate

from app.crud.user import user_create,login_user

from fastapi import APIRouter,Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse



router = APIRouter(tags=['Users'])

@router.post("/create")
def new_users(db:db_dependency,user:UserCreate):
    user_create(db,user)
    return JSONResponse(status_code=201,content={'message':'user create successfully'})

@router.post("/login")
def login_User(db:db_dependency,form_data: Annotated[OAuth2PasswordRequestForm,Depends()]):
    token =  login_user(db,form_data)
    return {
        "access_token":token,
        "token_type":"bearer"
    }