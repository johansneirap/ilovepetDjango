from django import forms
from .models import Cliente, Mascota
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = [
            'rut',
            'nombre',
            'numeroTelefono',
            'fechaNacimiento',
            'nacionalidad',
            'region',
            'comuna',
            'numeroContacto',
            'telefonoOficina',
            'profesion',
        ]
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'numeroTelefono': 'Numero de Teléfono',
            'correo': 'Correo',
            'fechaNacimiento': 'Fecha de nacimiento',
            'nacionalidad': 'Nacionalidad',
            'region': 'Región',
            'comuna': 'Comuna',
            'numeroContacto': 'Numero contacto',
            'telefonoOficina': 'Teléfono de oficina',
            'profesion': 'Profesión'
        }
        widgets = {
            'rut': forms.TextInput(attrs={'id': 'rut'}),
            'nombre': forms.TextInput(),
            'numeroTelefono':forms.NumberInput(),
            'correo':forms.EmailInput(),
            'fechaNacimiento':forms.DateTimeInput(),
            'nacionalidad': forms.Select(choices=(('Chilena', 'Chilena'),('Argentina', 'Argentina'),('Colombiana', 'Colombiana'))),
            'region': forms.Select(attrs={'id': 'regiones'}),
            'comuna': forms.Select(attrs={'id': 'comunas'}),
            'numeroContacto': forms.NumberInput(),
            'telefonoOficina': forms.NumberInput(),
            'profesion': forms.TextInput()
        }

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
            'rutMascota',
            'nombre',
            'sexo',
            'fechaNacimiento',
            'direccion',
            'tipo',
            'dueno'
        ]
        labels ={
            'rutMascota':'Rut',
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'fechaNacimiento': 'Fecha de nacimiento',
            'direccion': 'Direccion',
            'tipo': 'Tipo',
            'dueno': 'Dueño'
        }
        widgets = {
            'rutMascota': forms.TextInput(),
            'nombre': forms.TextInput(),
            'sexo': forms.Select(choices=(('','Seleccione sexo') ,('Macho', 'Macho'),('Hembra', 'Hembra'))),
            'fechaNacimiento': forms.SelectDateWidget(years=range(1980,datetime.now().year+1),empty_label=("Seleccione año", "Seleccione mes", "Seleccione dia")),
            'direccion': forms.TextInput(),
            'tipo': forms.Select(),
            'dueno': forms.Select()
        }

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['id'] = 'userTxt'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['id'] = 'userPwd'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'