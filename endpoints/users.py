from fastapi import APIRouter, Depends
from tortoise.contrib.fastapi import HTTPNotFoundError
from crud.user import get_by_id, get_all_users, create_new_user, get_current_user
from schemas.status import Status
from schemas.user_schema import User_Pydantic, User_In_Pydantic, User_Pydantic_List

router = APIRouter()


@router.post("/", response_model=Status)
async def create_user(user: User_In_Pydantic):
    return await create_new_user(user)


@router.get("/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_user_by_id(user_id: int):
    return await get_by_id(user_id)


@router.get("/", response_model=User_Pydantic_List)
async def get_users():
    return await get_all_users()


@router.get("/me", response_model=User_Pydantic)
async def get_me(user: User_Pydantic = Depends(get_current_user)):
    return user
