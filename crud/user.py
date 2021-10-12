from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from base.security import get_password_hash, verify_password, oauth2_scheme, SECRET_KEY, ALGORITHM
from models.users import User
from schemas.status import Status
from schemas.token import Login
from schemas.user_schema import User_Pydantic, User_Pydantic_List, User_In_Pydantic


async def get_by_email(email: str) -> User_Pydantic:
    return await User_Pydantic.from_queryset_single(User.get(email=email))


async def get_by_username(username: str) -> User_Pydantic:
    return await User_Pydantic.from_queryset_single(User.get(username=username))


async def get_by_id(user_id: int) -> User_Pydantic:
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


async def get_all_users() -> User_Pydantic_List:
    return await User_Pydantic_List.from_queryset(User.all())


async def create_new_user(user: User_In_Pydantic) -> Status:
    user_obj = await User.create(email=user.email,
                                 username=user.username,
                                 password=get_password_hash(user.password))
    await user_obj.save()
    if not user_obj:
        return Status(status_type="Error", message="Database error")
    return Status(status_type="Success", message=f"User {user.dict().get('username')} successfully created!")


async def authenticate_user(login: Login) -> User_Pydantic | bool:
    user_obj = await get_by_username(login.username)
    if not user_obj:
        return False
    if not verify_password(login.password, user_obj.dict().get('password')):
        return False
    return user_obj


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User_Pydantic:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = await get_by_email(email=payload.get('email'))
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )
    return user
