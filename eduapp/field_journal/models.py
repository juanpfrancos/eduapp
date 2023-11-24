from django.db import models
from django.utils import timezone

class Registro(models.Model):
    fecha = models.DateField(default=timezone.now)
    empleado = models.CharField(max_length=100)
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
