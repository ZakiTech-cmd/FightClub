from django.db import models


class Fighter(models.Model):
    picture = models.ImageField(null=True, blank=True, verbose_name='Imagine')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


