from django import forms
from .models import Student, Observations

class StudentForm(forms.ModelForm):
    temporary_photo = forms.FileField(required=False,
                                      widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    class Meta:
        model = Student
        fields = '__all__'
        

class ObservationsForm(forms.ModelForm):
    class Meta:
        model = Observations
        fields = ['date', 'observation']