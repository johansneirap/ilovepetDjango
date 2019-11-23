from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ClienteForm,MascotaForm, FormularioLogin
from .models import Mascota, TipoMascota, Galeria
from django.views.generic.edit import FormView,CreateView
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "web/registro.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('listado_mascotas')

class Login(FormView):
    template_name = 'web/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('usuario')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return super(Login,self).dispatch(request, *args, **kwargs)
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


@login_required()
def perfil(request):
    return render(request, 'web/perfil.html',{})

@login_required()
def usuario(request):
    if request.user.is_authenticated:
        username= request.user.username
        if username != "admin":
            global usuario_logeado
            usuario_logeado = username
    return render(request, 'web/usuario.html',{})

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
        form_user = UserCreationForm(request.POST)
        form = ClienteForm(request.POST)
        
        if form.is_valid() and form_user.is_valid() :
                user=form_user.save()
                user.email=user.username
                user.save()
                cliente = form.save(commit=False) 
                cliente.user = user

                cliente.save()

        return redirect('/accounts/login/')
    else:
        form = ClienteForm()
        form_user = UserCreationForm()
    context = {'form':form , 'form_user': form_user}
    return render(request,'web/registro2.html', context)

@login_required()
def registro_mascota(request):
    if request.method =='POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listado_mascotas')
    else:
        form=MascotaForm()

    return render(request, 'web/registro-mascota.html', {'form':form})

@login_required()
def listado_mascotas(request):
    tipos = TipoMascota.objects.all()
    if request.user.is_staff:
        if request.GET.get('featured'):
            featured_filter = request.GET.get('featured')
            mascotas = Mascota.objects.filter(sexo=featured_filter)
        elif request.GET.get('featured2'):
            featured_filter = request.GET.get('featured2')
            mascotas = Mascota.objects.filter(tipo=featured_filter)
        else:
            mascotas = Mascota.objects.all()
        contexto = {'mascotas':mascotas,'tipos':tipos}
        return render (request, 'web/mis-mascotas.html', contexto)
    else:
        if request.GET.get('featured'):
            featured_filter = request.GET.get('featured')
            mascotas = Mascota.objects.filter(sexo=featured_filter,dueno=request.user.cliente.rut)
        elif request.GET.get('featured2'):
            featured_filter = request.GET.get('featured2')
            mascotas = Mascota.objects.filter(tipo=featured_filter,dueno=request.user.cliente.rut)
        else:
            mascotas = Mascota.objects.filter(dueno=request.user.cliente.rut)
        contexto = {'mascotas':mascotas,'tipos':tipos}
    return render (request, 'web/mis-mascotas.html', contexto)

@login_required()
def actualizar_mascota(request, rutMascota):
    mascota = Mascota.objects.get(rutMascota=rutMascota)
    if request.method == "GET":
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('listado_mascotas')
    return render(request, 'web/registro-mascota.html',{'form':form})

@login_required()
def eliminiar_mascota(request, rutMascota):
    mascota = Mascota.objects.get(rutMascota=rutMascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect ('listado_mascotas')
    return render(request, 'web/eliminar-mascota.html',{'mascota':mascota})

