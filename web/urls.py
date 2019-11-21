from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home,name='index'),
    path('galeria.html', views.galeria,name='galeria'),
    path('planes.html', views.planes,name='planes'),
    path('quienes-somos.html', views.about,name='quienes-somos'),
    path('registro.html', views.registro,name='registro'),
    path('registro2.html', views.registro2,name='registro2'),
    path('registro-mascota.html', views.registro_mascota,name='registro_mascota')
]