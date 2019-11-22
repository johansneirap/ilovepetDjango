from django.contrib import admin
from web.models import Cliente, Mascota, TipoMascota, Galeria
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(TipoMascota)
admin.site.register(Galeria)