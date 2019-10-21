from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'web/home.html',{})

def galeria(request):
    return render(request, 'web/galeria.html')

def planes(request):
    return render(request, 'web/planes.html')

def about(request):
    return render(request, 'web/quienes-somos.html')

def registro(request):
    return render(request, 'web/registro.html')

