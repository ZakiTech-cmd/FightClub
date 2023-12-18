from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Fighter
from .permissions import IsFighterOwnerOrReadOnly
from .serializers import FighterSerializer
from django_filters.rest_framework import DjangoFilterBackend


class FighterViewSet(ModelViewSet):
    queryset = Fighter.objects.select_related("owner").all()
    serializer_class = FighterSerializer
    permission_classes = [IsFighterOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



