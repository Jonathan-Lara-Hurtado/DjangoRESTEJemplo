from django.shortcuts import render


from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions
from administrador.serializers import UsuarioSerializador,GrupoSerializador


class UsuarioVistaSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')    
    serializer_class = UsuarioSerializador
    permission_classes  = [permissions.IsAuthenticated]


class GrupoVistaSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GrupoSerializador
    permission_classes = [permissions.IsAuthenticated]

