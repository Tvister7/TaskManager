from fastapi import APIRouter, Depends
from crud.task import create_new_task, get_all_tasks, get_all_current_user_tasks, update_user_task, delete_user_task
from crud.user import get_current_user
from schemas.status import Status
from schemas.task_schema import Task_In_Pydantic, Task_Pydantic, Task_Pydantic_List
from schemas.user_schema import User_Pydantic

router = APIRouter()


@router.post("/", response_model=Status, status_code=201)
async def create_task(task: Task_In_Pydantic, user: User_Pydantic = Depends(get_current_user)):
    return await create_new_task(task, user.dict().get('id'))


@router.get("/all", response_model=Task_Pydantic_List)
async def all_tasks():
    return await get_all_tasks()


@router.get("/all_my", response_model=Task_Pydantic_List)
async def all_my_tasks(user: User_Pydantic = Depends(get_current_user)):
    return await get_all_current_user_tasks(user.dict().get('id'))


@router.put("/update/{task_id}", response_model=Status)
async def update_task(task_id: int, new_data: Task_In_Pydantic, user: User_Pydantic = Depends(get_current_user)):
    await update_user_task(task_id, new_data, user.dict().get('id'))
    return


@router.delete("/delete/{task_id}", response_model=Status)
async def delete_task(task_id: int, user: User_Pydantic = Depends(get_current_user)):
    return await delete_user_task(task_id, user.dict().get('id'))
