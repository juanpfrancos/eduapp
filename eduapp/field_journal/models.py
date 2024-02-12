from django.db import models
from django.utils import timezone
from accounts.models import CustomUser

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=timezone.now)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    enough_time = models.BooleanField()
    interesting_activities = models.BooleanField()
    nice_materials = models.BooleanField()
    outside_working = models.BooleanField()
    involved = models.CharField(
        max_length=10,
        choices=[('TODOS', 'TODOS'), ('ALGUNOS', 'ALGUNOS'), ('POCOS', 'POCOS')]
    )
    attentive = models.CharField(
        max_length=10,
        choices=[('TODOS', 'TODOS'), ('ALGUNOS', 'ALGUNOS'), ('POCOS', 'POCOS')]
    )
    interruptions = models.BooleanField()
    influences = models.TextField()
    relevant_situation = models.TextField()

    def __str__(self):
        return f"{self.fecha} - {self.empleado}"
