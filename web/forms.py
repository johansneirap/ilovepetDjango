from django import forms
from .models import Cliente, Mascota
from datetime import datetime

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = [
            'rut',
            'nombre',
            'numeroTelefono',
            'correo',
            'fechaNacimiento',
            'nacionalidad',
            'region',
            'comuna',
            'numeroContacto',
            'telefonoOficina',
            'profesion'
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
            'nacionalidad': forms.TextInput(),
            'region': forms.TextInput(),
            'comuna': forms.TextInput(),
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
            'sexo': forms.TextInput(),
            'fechaNacimiento': forms.SelectDateWidget(years=range(1980,datetime.now().year+1),empty_label=("Seleccione año", "Seleccione mes", "Seleccione dia")),
            'direccion': forms.TextInput(),
            'tipo': forms.Select(),
            'dueno': forms.Select()
        }

