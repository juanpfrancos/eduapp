from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    active = models.BooleanField(default=True)
    picture = models.CharField(max_length=100)
    rh = models.CharField(max_length=2)
    alergies = models.CharField(max_length=100)
    medications = models.CharField(max_length=100)
    
    def get_observations(self):
        return Observations.objects.filter(student=self)

class Observations(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    observation = models.CharField(max_length=100)