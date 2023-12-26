from django import forms
from .models import Student, Observations

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ObservationsForm(forms.ModelForm):
    class Meta:
        model = Observations
        fields = ['date', 'observation']