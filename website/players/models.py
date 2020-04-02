from django.db import models

# Create your models here.
# This is the base player class that all players will be based on
class Player(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField(default = -1)
    
    def __str__(self):
        return self.last_name + ", " + self.first_name

class Team(models.Model):
    #will contain info like record
    team_name = models.CharField(max_length = 15)
    team_short_name = models.CharField(max_length = 2)

    def __str__(self):
        return self.team_short_name

