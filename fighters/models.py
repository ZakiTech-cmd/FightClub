from django.db import models

from users.models import User


# Create your models here.


class Fighter(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    weight = models.IntegerField()
    height = models.IntegerField()
    birth_date = models.DateField()

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
