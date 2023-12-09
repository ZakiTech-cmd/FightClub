from django.utils import timezone
from rest_framework import serializers

from fighters.models import Fighter, Title, Match


class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = ['id', 'picture', 'first_name', 'last_name', 'nation', 'weight', 'height', 'birth_date']

    def validate_birth_date(self, value):
        if value >= timezone.now().date():
            raise serializers.ValidationError("Birthday should be in the past")
        return value


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['id', 'fighter', 'name']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'challenger', 'defender', 'result', 'date']
