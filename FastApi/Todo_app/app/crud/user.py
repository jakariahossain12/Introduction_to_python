from sqlalchemy.orm import Session
import app.models as models
from app.schemas.user import UserCreate
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

def user_create(db:Session,new_user:UserCreate):
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