from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(max_length=12,primary_key=True)
    nombre =models.CharField(max_length=50)
    numeroTelefono = models.IntegerField()
    correo = models.EmailField(unique=True)
    fechaNacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=20)
    region = models.CharField(max_length=25)
    comuna = models.CharField(max_length=30)
    numeroContacto = models.IntegerField()
    telefonoOficina = models.IntegerField()
    profesion = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.rut)

class TipoMascota(models.Model):
    nombre= models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nombre)
        
class Mascota(models.Model):
    rutMascota = models.CharField(max_length= 10,primary_key=True)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    fechaNacimiento = models.DateField(null=True,blank=True)
    direccion = models.CharField(max_length=50)
    dueno = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMascota, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.rutMascota)

class Galeria(models.Model):
    image = models.ImageField(upload_to='galeria', blank=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.descripcion)