from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
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
    def get_by_user(self, request, pk = None):
        #queryset = Sesiones.objects.all()
        session = Sesiones.objects.filter(IdUsuario = pk)
        page = self.paginate_queryset(session)
        if page is not None:
            serializer = self.get_serializer(page, many = True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(session, many = True)
        return Response(serializer.data)

    # @action(detail=True, methods=['post'])
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = SesionesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print("Create ", serializer.data['id'])
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class CuentasEnlazadasViewSet(viewsets.ModelViewSet):
    serializer_class = CuentasEnlazadasSerializer
    queryset = CuentasEnlazadas.objects.all()

