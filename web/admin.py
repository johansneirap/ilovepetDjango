from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import admin
from web.models import Cliente, Mascota, TipoMascota, Galeria
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(TipoMascota)
admin.site.register(Galeria)