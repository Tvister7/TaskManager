from tortoise.models import Model
from tortoise.fields import CharField, IntField


class User(Model):
    id = IntField(pk=True)
    email = CharField(max_length=100, unique=True)
    username = CharField(max_length=100)
    password = CharField(max_length=256)

