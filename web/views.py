from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ClienteForm,MascotaForm
from .models import Galeria
# Create your views here.
def home(request):
    return render(request, 'web/home.html',{})

def galeria(request):
    galerias = Galeria.objects.all()
    return render(request, 'web/galeria.html', {'galerias': galerias})

def planes(request):
    return render(request, 'web/planes.html')

def about(request):
    return render(request, 'web/quienes-somos.html')

def registro(request):
    return render(request, 'web/registro.html')

def registro2(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = ClienteForm()
    
    return render(request,'web/registro2.html', {'form':form})

def registro_mascota(request):
    if request.method =='POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form=MascotaForm()

    return render(request, 'web/registro-mascota.html', {'form':form})
