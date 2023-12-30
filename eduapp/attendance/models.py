from django.db import models
from students.models import Student


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    attended = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.student.name} - {self.date}"