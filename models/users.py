from tortoise.models import Model
from tortoise.fields import CharField, IntField


class User(Model):
    id = IntField(pk=True)
    email = CharField(max_length=100, unique=True)
    full_name = CharField(max_length=100)
    hashed_password = CharField(max_length=256)

