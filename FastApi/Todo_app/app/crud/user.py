from sqlalchemy.orm import Session
import app.models as models
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from fastapi import HTTPException,status
from datetime import timedelta
from app.auth.jwt_token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

def user_create(db:Session,new_user:UserCreate):

    existing_username = db.query(models.user.Users).filter(models.user.Users.username == new_user.username).first()
    if existing_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    # 2. Check if email already exists
    existing_email = db.query(models.user.Users).filter(models.user.Users.email == new_user.email).first()
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")



    user_model = models.user.Users(
        email = new_user.email,
        username = new_user.username,
        firstname = new_user.firstname,
        lastname = new_user.lastname,
        hash_password = bcrypt_context.hash(new_user.password),
        is_active = True,
        role =  new_user.role
    )
    
    db.add(user_model)
    db.commit()
    db.refresh(user_model)


def login_user(db:Session,form_data:OAuth2PasswordRequestForm):
    user = db.query(models.user.Users).filter(models.user.Users.username == form_data.username).first()

    if user is None:
        raise HTTPException(status_code=404,detail="user not found")
    
    if bcrypt_context.verify(form_data.password,user.hash_password):
        token = create_access_token(user.username,user.id,user.role,timedelta(minutes=30))
        return token
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="password did not match")