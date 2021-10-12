from datetime import timedelta, datetime
from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from base.security import make_token
from crud.user import authenticate_user
from schemas.token import Token, Login

router = APIRouter()


@router.post("/", response_model=Token, status_code=201)
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), expires_delta: Optional[timedelta] = None):
    user_obj = await authenticate_user(Login(username=form_data.username, password=form_data.password))

    if not user_obj:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    user_obj.dict().update({"expire": expire})

    token = make_token(user_obj)

    return Token(access_token=token, token_type='bearer')
