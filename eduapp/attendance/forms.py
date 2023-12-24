from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['attended']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attended'].label = 'Asistió'