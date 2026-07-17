from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    email: str
    username: str
    firstname: str
    lastname: str
    password: str
    role: str