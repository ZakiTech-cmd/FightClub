from django.utils import timezone
from rest_framework import serializers

from fighters.models import Fighter, Title, Match


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class FighterSerializer(serializers.ModelSerializer):
    title = TitleSerializer()

    class Meta:
        model = Fighter
        fields = '__all__'

    def validate_birth_date(self, value):
        if value >= timezone.now().date():
            raise serializers.ValidationError("Birthday should be in the past")
        return value


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
