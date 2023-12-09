from django.utils import timezone
from rest_framework import serializers

from fighters.models import Fighter


class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = ['id', 'picture', 'first_name', 'last_name', 'nation', 'weight', 'height', 'birth_date']

    def validate_birth_date(self, value):

        if value >= timezone.now().date():
            raise serializers.ValidationError("Birthday date should be in the past")
        return value
