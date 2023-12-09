from django.db import models


# Create your models here.


class Fighter(models.Model):
    picture = models.ImageField(null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    weight = models.IntegerField()
    height = models.IntegerField()
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Title(models.Model):
    fighter = models.ForeignKey(Fighter, default=None, on_delete=models.CASCADE)
    name = models.CharField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Match(models.Model):
    challenger = models.ForeignKey(Fighter, default=None, on_delete=models.CASCADE, related_name="Fighter1")
    defender = models.ForeignKey(Fighter, default=None, on_delete=models.CASCADE, related_name="Fighter2")
    result = models.CharField()
    date = models.DateField()

    def __str__(self):
        return self.challenger