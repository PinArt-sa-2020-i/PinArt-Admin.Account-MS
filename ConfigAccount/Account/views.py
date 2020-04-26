from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from jwcrypto import jwt, jwk
from .models import TipoNotificacion, ConfigNotificaciones, Medio, Sesiones, CuentasEnlazadas
from .serializers import TipoNotificacionSerializer, ConfigNotificacionesSerializer, MedioSerializer, SesionesSerializer, CuentasEnlazadasSerializer
import json

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

    @action(detail=False, methods=['get'])
    def get_by_user(self, request):
        key = jwk.JWK(kty = 'oct', k = 'pinart20')
        key.export()
        token = request.headers['auth']
        st = jwt.JWT(key = key, jwt = token)
        result = json.loads(st.claims)
        sessionID = int(result['sessionID'])
        session = get_object_or_404(self.queryset, pk = sessionID)
        serializer = SesionesSerializer(session)
        if serializer.data['Activo']:
            return Response(serializer.data['IdUsuario'])
        else:
            error = {
                'message' : 'Sesion Inactiva'
            }
            return Response(error, status = status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = SesionesSerializer(data = request.data)
        key = jwk.JWK(kty = 'oct', k = 'pinart20')
        key.export()
        if serializer.is_valid():
            serializer.save()
            sessionid = serializer.data['id']
            userid = serializer.data['IdUsuario']
            user = {
                'userID' : userid,
                'sessionID' : sessionid
            }
            Token = jwt.JWT(header = {'alg' : 'HS256'}, claims = user)
            Token.make_signed_token(key)
            result = Token.serialize()
            response = {
                'data' : serializer.data,
                'Token' : result  
            }
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class CuentasEnlazadasViewSet(viewsets.ModelViewSet):
    serializer_class = CuentasEnlazadasSerializer
    queryset = CuentasEnlazadas.objects.all()

