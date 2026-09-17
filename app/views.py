from django.shortcuts import render
from rest_framework import viewsets
from .models import Grupo, Material
from .serializers import GrupoSerializer, Material

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = GrupoSerializer
