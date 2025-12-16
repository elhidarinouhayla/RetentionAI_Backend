from jose import jwt
from fastapi import HTTPException, Header
from .config import SECRET_KEY, ALGORITHM
from passlib.context import CryptContext


def create_token(username:str):
    paylod = {
        "sub": username
        }
    token = jwt.encode(paylod,SECRET_KEY,algorithm=ALGORITHM)
    return token


def verify_token(token: str = Header(...)):
    try:
        paylod = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        return paylod
    except:
        raise HTTPException(status_code=400, detail="le token est invalide")
    


    