from fastapi import HTTPException

from models.tasks import Task
from schemas.status import Status
from schemas.task_schema import Task_Pydantic, Task_In_Pydantic, Task_Pydantic_List


async def get_task_by_id(task_id: int) -> Task_Pydantic:
    return await Task_Pydantic.from_queryset_single(Task.get(id=task_id))


async def create_new_task(task: Task_In_Pydantic, creator_id: int) -> Status:
    task_obj = await Task.create(name=task.name,
                                 about=task.about,
                                 expired_at=task.expired_at,
                                 creator_id=creator_id)
    await task_obj.save()
    if not task_obj:
        return Status(status_type="Error", message="Database error")
    return Status(status_type="Success", message=f"Task {task.dict().get('name')} successfully created!")


async def get_all_tasks() -> Task_Pydantic_List:
    return await Task_Pydantic_List.from_queryset(Task.all())


async def get_all_current_user_tasks(user_id: int) -> Task_Pydantic_List:
    return await Task_Pydantic_List.from_queryset(Task.filter(creator_id=user_id))


async def update_user_task(task_id: int, new_data: Task_In_Pydantic, user_id: int) -> Status:
    task_to_update_obj = await Task.filter(id=task_id).first()
    if not task_to_update_obj:
        raise HTTPException(status_code=404, detail='Task is not exists')
    if task_to_update_obj.creator_id != user_id:
        raise HTTPException(status_code=401, detail='Task update is allowed only for creator')
    await Task.filter(id=task_id).update(**new_data.dict(exclude_unset=True))
    return Status(status_type="Success", message="Task №{task_id} is updated!")


async def delete_user_task(task_id: int, user_id: int) -> Status:
    task_to_update_obj = await Task.filter(id=task_id).first()
    if not task_to_update_obj:
        raise HTTPException(status_code=404, detail='Task is not exists')
    if task_to_update_obj.creator_id != user_id:
        raise HTTPException(status_code=401, detail='Task update is allowed only for creator')
    await Task.filter(id=task_id).delete()
    return Status(status_type="Success", message=f"Task №{task_id} is deleted!")
