from django.db import models

# Create your models here.
# This is the base player class that all players will be based on
class Player(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, default = 1)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    composite = models.FloatField(default = 0)
    past_points = models.FloatField(default = 0)
    past_PPG = models.FloatField(default = 0)
    projected_rank = models.IntegerField(default = 0)
    games = models.IntegerField(default = 0)
    tier = models.IntegerField(default = 0)
    pos_tier = models.IntegerField(default = 0)

    def FieldList(self):
        ret = {val.name: val.value_to_string(self) for val in self._meta.get_fields()}
        try:
            ret["team"] = Team.objects.get(id = ret["team"]).team_short_name;
        except Team.DoesNotExist:
            ret["team"] = "None"
        ret.pop("id")
        return ret

    def __str__(self):
        return self.last_name + ", " + self.first_name

    class Meta:
        abstract = True

class Team(models.Model):
    #will contain info like record
    team_name = models.CharField(max_length = 15)
    team_short_name = models.CharField(max_length = 3)

    def __str__(self):
        return self.team_short_name

class Quarterback(Player):
    completions = models.IntegerField(default = 0)
    attempts = models.IntegerField(default = 0)
    yards = models.IntegerField(default = 0)
    touchdowns = models.IntegerField(default = 0)
    interceptions = models.IntegerField(default = 0)
    rushing_attempts = models.IntegerField(default = 0)
    rushing_yds = models.IntegerField(default = 0)
    rushing_touchdowns = models.IntegerField(default = 0)

class RunningBack(Player):
    rushing_attempts = models.IntegerField(default = 0)
    rushing_yds = models.IntegerField(default = 0)
    rushing_touchdowns = models.IntegerField(default = 0)
    targets = models.IntegerField(default = 0)
    receptions = models.IntegerField(default = 0)
    rec_yards = models.IntegerField(default = 0)
    rec_touchdowns = models.IntegerField(default = 0)

class WideReceiver(Player):
    targets = models.IntegerField(default = 0)
    receptions = models.IntegerField(default = 0)
    rec_yards = models.IntegerField(default = 0)
    rec_touchdowns = models.IntegerField(default = 0)
    rushing_attempts = models.IntegerField(default = 0)
    rushing_yds = models.IntegerField(default = 0)
    rushing_touchdowns = models.IntegerField(default = 0)

class TightEnd(Player):
    targets = models.IntegerField(default = 0)
    receptions = models.IntegerField(default = 0)
    rec_yards = models.IntegerField(default = 0)
    rec_touchdowns = models.IntegerField(default = 0)

class Kicker(Player):
    FGM = models.IntegerField(default = 0)
    FGA = models.IntegerField(default = 0)
    EPM = models.IntegerField(default = 0)
    EPA= models.IntegerField(default = 0)
    def FG_PCT(self):
        if self.FGA != 0:
            return self.FGM / self.FGA
        else:
            return 0
    
    def EP_PCT(self):
        if self.EPA != 0:
            return self.EPM / self.EPA
        else:
            return 0

    def FieldList(self):
        ret = super().FieldList()
        ret["FG PCT"] = self.FG_PCT()
        ret["EP PCT"] = self.EP_PCT()
        return ret
    

class Defense(Player):
    games = models.IntegerField(default = 0)
    sacks = models.IntegerField(default = 0)
    FR = models.IntegerField(default = 0)
    interceptions = models.IntegerField(default = 0)
    touchdowns = models.IntegerField(default = 0)
    passing_ypg = models.FloatField(default = 0)
    rushing_ypg = models.FloatField(default = 0)
    safeties = models.IntegerField(default = 0)
    kickoff_touchdowns = models.IntegerField(default = 0)

    def FieldList(self):
        ret = super().FieldList()
        ret.pop("first_name")
        ret.pop("last_name")
        return ret
    
    def __str__(self):
        return self.team.team_short_name
