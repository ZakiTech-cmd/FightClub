from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from matches.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

    def validate(self, attrs):
        challenger = None
        defender = None

        if self.instance:
            challenger = self.instance.challenger
            defender = self.instance.defender

        if "challenger" in attrs:
            challenger = attrs['challenger']

        if "defender" in attrs:
            defender = attrs['defender']

        if challenger == defender:
            raise ValidationError("Challenger must be different from Defender")

        return attrs
