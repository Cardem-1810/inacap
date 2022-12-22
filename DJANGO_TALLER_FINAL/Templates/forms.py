from dataclasses import fields
from socket import fromshare
from django import forms
from Templates.models import Reservas

class FormReservas(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'
