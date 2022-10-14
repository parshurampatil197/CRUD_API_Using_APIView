from django.db import models
from .common_models import CommenFields


class Student(CommenFields):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    roll_number = models.IntegerField(unique=True)
    mobile = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

