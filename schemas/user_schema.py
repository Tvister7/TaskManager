from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from models.users import User

User_Pydantic = pydantic_model_creator(User, name="User")
User_In_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
User_Pydantic_List = pydantic_queryset_creator(User)
