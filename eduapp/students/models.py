from django.db import models
from schools.models import School

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    active = models.BooleanField(default=True)
    rh = models.CharField(max_length=2)
    alergies = models.CharField(max_length=100)
    medications = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def get_observations(self):
        return Observations.objects.filter(student=self)

class Observations(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    observation = models.CharField(max_length=100)