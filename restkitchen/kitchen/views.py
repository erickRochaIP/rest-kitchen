from django.shortcuts import render
from rest_framework import generics
from .models import Receita
from .serializers import ReceitaSerializer

# Create your views here.
class ReceitaList(generics.ListCreateAPIView):

    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer