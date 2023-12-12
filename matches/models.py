from django.db import models

from fighters.models import Fighter

MATCH_RESULT = [
    ("To be disputed", "To be disputed"),
    ("Challenger", "Challenger"),
    ("Defender", "Defender"),
    ("Draw", "Draw"),
]


# Create your models here.
class Match(models.Model):
    challenger = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="challenger_matches")
    defender = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="defender_matches")
    result = models.CharField(choices=MATCH_RESULT, default="To be disputed")
    date = models.DateField()
