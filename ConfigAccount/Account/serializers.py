from rest_framework import serializers
from .models import TipoNotificacion, ConfigNotificaciones, Medio, Sesiones, CuentasEnlazadas

class TipoNotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNotificacion
        fields = '__all__'

class ConfigNotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigNotificaciones
        fields = '__all__'

class MedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio
        fields = '__all__'


class SesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesiones
        fields = '__all__'

class CuentasEnlazadasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CuentasEnlazadas
        fields = '__all__'