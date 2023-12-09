from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Fighter
from .serializers import FighterSerializer


class FighterListCreateView(generics.ListCreateAPIView):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer


class FighterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer
