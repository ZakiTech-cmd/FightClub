from django.utils import timezone
from rest_framework import serializers

from fighters.models import Fighter
from titles.serializers import TitleSerializer


class FighterSerializer(serializers.ModelSerializer):
    # titles = TitleSerializer(many=True, required=False)
    club_name = serializers.ReadOnlyField(source="owner.club_name")

    class Meta:
        model = Fighter
        fields = '__all__'
        read_only_fields = ['owner']

    def validate_birth_date(self, value):
        if value >= timezone.now().date():
            raise serializers.ValidationError("Birthday should be in the past")
        return value


