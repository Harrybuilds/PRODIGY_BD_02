from django.db import models
from uuid import uuid4 as uuid

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    id = models.UUIDField(default=uuid, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f'name: {self.name} email:{self.email}'
