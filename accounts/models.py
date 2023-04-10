from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    # Relacionamento 1:1 com o User padrão
    user = models.OneToOneField(User, on_delete=models.CASCADE)
