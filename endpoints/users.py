from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from crud.user import get_all_users, create_new_user, get_current_user
from schemas.status import Status
from schemas.user_schema import User_Pydantic, User_In_Pydantic

router = APIRouter()


@router.post("/", response_model=Status, status_code=201)
async def create_user(user: User_In_Pydantic):
    return await create_new_user(user)


@router.get("/", response_model=Page[User_Pydantic])
async def get_users():
    users = await get_all_users()
    dict_users = users.dict().get('__root__')
    return paginate(dict_users)


@router.get("/me", response_model=User_Pydantic)
async def get_me(user: User_Pydantic = Depends(get_current_user)):
    return user
