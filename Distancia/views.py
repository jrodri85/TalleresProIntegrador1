from django.shortcuts import render

from rest_framework import viewsets
from .models import Distancia
from .serializers import DistanciaSerializer

class DistanciaViewSet(viewsets.ModelViewSet):
    queryset = Distancia.objects.all().order_by('-created')
    serializer_class = DistanciaSerializer
# Create your views here.
