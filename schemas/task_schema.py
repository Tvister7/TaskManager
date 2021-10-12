from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from models.tasks import Task

Task_Pydantic = pydantic_model_creator(Task, name="Task")
Task_In_Pydantic = pydantic_model_creator(Task, name="TaskIn", exclude_readonly=True)
Task_Pydantic_List = pydantic_queryset_creator(Task)
