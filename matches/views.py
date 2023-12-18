from django.db.models import Q
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from utils.permissions import IsAdminOrReadOnly
from .models import Match
from .serializers import MatchSerializer


class MatchFilter(filters.FilterSet):
    owner = filters.NumberFilter(method="owner_filter")
    fighter = filters.NumberFilter(method="fighter_filter")

    class Meta:
        model = Match
        fields = ['owner', 'fighter']

    def owner_filter(self, queryset, name, value):
        return queryset.filter(Q(challenger__owner=value) | Q(defender__owner=value))

    def fighter_filter(self, queryset, name, value):
        return queryset.filter(Q(challenger=value) | Q(defender=value))


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MatchFilter
