from django.contrib import admin
from .models import TipoNotificacion, ConfigNotificaciones, Medio, Sesiones, CuentasEnlazadas

admin.site.register(TipoNotificacion)
admin.site.register(ConfigNotificaciones)
admin.site.register(Medio)
admin.site.register(Sesiones)
admin.site.register(CuentasEnlazadas)
# Register your models here.
