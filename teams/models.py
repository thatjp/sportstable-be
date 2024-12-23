from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=255)
    team_id = models.IntegerField()

    def __str__(self) -> str:
        return self.name