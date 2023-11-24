from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        exclude = ['fecha']  # Excluye el campo fecha para que no lo modifiquen
