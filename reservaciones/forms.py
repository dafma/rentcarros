from .models import Cliente, Reservacion, Tarjeta
from django import forms

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellidos', 'email', 'num_tel')


class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ('fecha_inicio', 'fecha_termino','carro')
        widgets={
            'fecha_inicio': forms.TextInput(attrs={'type': 'text', "class": "form-control", 'id': 'datepicker1'}),
            'fecha_termino': forms.TextInput(attrs={'type': 'text', "class": "form-control", 'id': 'datepicker2'}),
            'carro': forms.TextInput(attrs={'type': 'hidden', 'readonly': 'readonly'}),

        }

class ReservacionPanel(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ('fecha_inicio',)
        widgets = {
            'fecha_inicio': forms.TextInput(attrs={'type': 'text', "class": "form-control", 'id': 'datepicker3'}),

        }

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ("num_tarjeta", "codigo_cvc", "fecha_expiracion", "terminos_condiciones")
        widgets= {
            "num_tarjeta": forms.NumberInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder':'Tarjeta de credito valida.'}),
            "codigo_cvc": forms.NumberInput(attrs={'type':'date', 'class': 'form-control'}),
            "fecha_expiracion": forms.DateInput(attrs={'type': 'number', 'class': 'form-control', }),
            "terminos_condiciones": forms.CheckboxInput(attrs={"required": "true"}),
        }
