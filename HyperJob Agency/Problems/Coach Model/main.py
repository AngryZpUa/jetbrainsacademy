from django.db import models
from django.db.models import CharField, ForeignKey, IntegerField


class Team(models.Model):
    name = CharField(max_length=64)

    class Meta:
        app_label = 'tournament'


class Coach(models.Model):
    name = models.CharField(max_length=48)
    experience = IntegerField()
    team = ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        app_label = 'tournament'