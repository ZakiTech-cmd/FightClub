from django.db import models

from fighters.models import Fighter


# Create your models here.
class Match(models.Model):
    challenger = models.ForeignKey(Fighter, default=None, on_delete=models.CASCADE, related_name="challenger_matches")
    defender = models.ForeignKey(Fighter, default=None, on_delete=models.CASCADE, related_name="defender_matches")
    result = models.CharField()
    date = models.DateField()

    def __str__(self):
        return self.challenger
