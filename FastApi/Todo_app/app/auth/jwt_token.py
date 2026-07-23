from jose import jwt,JWTError
from datetime import timedelta,datetime,timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from typing import Annotated

SECRET_KEY = 'cd0d6d91ca2e4049038c3c91d48db13dff57c8c0f4bed3701e789dcc9ed82cd6'

ALGORITHM = 'HS256'

OAuth2_bearer = OAuth2PasswordBearer(tokenUrl='/login')

def create_access_token(username:str,user_id:int,role:str,expires_delta:timedelta):
    encode = {'sub':username, 'id':user_id,'role':role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

def get_current_user(token:Annotated[str,Depends(OAuth2_bearer)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username = payload.get('sub')
        user_id = payload.get('id')
        role = payload.get('role')
        
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User not found')
        
        return {'username':username,'id':user_id,'role':role}
    except JWTError as e:
        print('jwt error ',e)
        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid token')
        
