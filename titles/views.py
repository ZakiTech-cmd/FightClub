from django.shortcuts import render
from rest_framework import generics

from titles.models import Title
from titles.serializers import TitleSerializer


# Create your views here.
class TitleListCreateView(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class TitleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
