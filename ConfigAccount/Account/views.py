from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoNotificacion, ConfigNotificaciones, Medio, Sesiones, CuentasEnlazadas
from .serializers import TipoNotificacionSerializer, ConfigNotificacionesSerializer, MedioSerializer, SesionesSerializer, CuentasEnlazadasSerializer

class TipoNotificacionViewSet(viewsets.ModelViewSet):
    serializer_class = TipoNotificacionSerializer
    queryset = TipoNotificacion.objects.all()

class ConfigNotificacionesViewSet(viewsets.ModelViewSet):
    serializer_class = ConfigNotificacionesSerializer
    queryset = ConfigNotificaciones.objects.all()

class MedioViewSet(viewsets.ModelViewSet):
    serializer_class = MedioSerializer
    queryset = Medio.objects.all()

class SesionesViewSet(viewsets.ModelViewSet):
    serializer_class = SesionesSerializer
    queryset = Sesiones.objects.all()

    @action(detail=True, methods=['get'])
    def get_by_user(self, request, pk=None):
        session = get_object_or_404(queryset,IdUsuario = pk)
        serializer = SesionesSerializer(session)
        return Response(serialize.data)

class CuentasEnlazadasViewSet(viewsets.ModelViewSet):
    serializer_class = CuentasEnlazadasSerializer
    queryset = CuentasEnlazadas.objects.all()

