from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    game_link = models.CharField(max_length=500)
    def __str__(self):
        return self.name
