from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Fighter
from .permissions import IsFighterOwnerOrReadOnly
from .serializers import FighterSerializer


class FighterViewSet(ModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer
    permission_classes = [IsFighterOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



