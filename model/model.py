from tortoise import fields, Tortoise
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Car(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50, unique=True)
    model = fields.CharField(50)

    def __str__(self) -> str:
        return self.name


Car_dant = pydantic_model_creator(Car, name='Car')
CarIn_dant = pydantic_model_creator(Car, name='CarIn', exclude_readonly=True)
