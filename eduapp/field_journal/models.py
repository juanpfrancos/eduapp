from django.db import models
from django.utils import timezone
from accounts.models import CustomUser

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)
    empleado = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tiempo_suficiente = models.BooleanField()
    actividades_interesantes = models.BooleanField()
    material_agradable = models.BooleanField()
    trabajo_fuera_aula = models.BooleanField()
    involucrados = models.CharField(
        max_length=10,
        choices=[('TODOS', 'TODOS'), ('ALGUNOS', 'ALGUNOS'), ('POCOS', 'POCOS')]
    )
    atentos = models.CharField(
        max_length=10,
        choices=[('TODOS', 'TODOS'), ('ALGUNOS', 'ALGUNOS'), ('POCOS', 'POCOS')]
    )
    interrupciones = models.BooleanField()
    influencias = models.TextField()
    situacion_relevante = models.TextField()

    def __str__(self):
        return f"{self.fecha} - {self.empleado}"
