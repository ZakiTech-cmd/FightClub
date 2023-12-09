from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Fighter, Match, Title
from .serializers import FighterSerializer, MatchSerializer, TitleSerializer


class FighterListCreateView(generics.ListCreateAPIView):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer


class FighterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer


class TitleListCreateView(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class TitleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class MatchListCreateView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
