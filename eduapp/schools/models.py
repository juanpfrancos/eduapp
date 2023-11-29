from django.db import models
from django.utils import timezone

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name_school = models.CharField(max_length=90, unique=True)
    date = models.DateField(default=timezone.now)
    nit = models.CharField(max_length=40)
    address = models.CharField(max_length=90)

    def __str__(self):
        return f"{self.name_school}"