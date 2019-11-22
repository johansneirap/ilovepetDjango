from django.test import TestCase,Client
from .models import Cliente,Mascota,TipoMascota
from .forms import ClienteForm
from django.urls import reverse
from django.contrib.auth.models import User

class GestionUsuarioTest(TestCase):
    def setUp(self):
        self.cliente = Client()
        User.objects.create_user('Johans',password='1234')
    
    def test_login(self):
        response = self.cliente.post(
            reverse('login'),{'username':'Johans','password':'1234'})
        self.assertEqual(response.status_code, 302, 'No es el codigo correcto')

class TipoMascotaTest(TestCase):

    def test_crearTipoMuchosCaracteres(self):
        tipoNuevo = TipoMascota(nombre='Este es un tipo de mascota demasiado largo para caer en este campo de texto')
        tipoNuevo.save()
        existe = False
        if tipoNuevo:
            existe=True
            
        self.assertEqual(existe,False,'El tipo de mascota ingresado es demasiado largo '+str(len(str(tipoNuevo.nombre))))
