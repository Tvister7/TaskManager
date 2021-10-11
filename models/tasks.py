from tortoise.models import Model
from tortoise.fields import CharField, IntField, DatetimeField, ForeignKeyField


class Task(Model):
    id = IntField(pk=True)
    name = CharField(max_length=200)
    about = CharField(max_length=500)
    created_at = DatetimeField(auto_now_add=True)
    expired_at = DatetimeField()
    creator = ForeignKeyField("models.User", related_name="tasks")

    class PydanticMeta:
        exclude = ("created_at", )
