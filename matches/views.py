import random
from datetime import date, timedelta

from django.db.models import Q
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from fighters.models import Fighter
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

    @action(methods=["POST"], detail=False, url_path="random")
    def random_match(self, request):
        if Fighter.objects.count() < 2:
            raise ValidationError("You don't have enough fighters.")

        challenger = Fighter.objects.order_by("?").first()
        defender = Fighter.objects.exclude(id=challenger.id).order_by("?").first()
        random_days = random.randint(1, 30)
        future_date = date.today() + timedelta(days=random_days)
        match = Match.objects.create(challenger=challenger, defender=defender, date=future_date)

        return Response(MatchSerializer(match).data)
