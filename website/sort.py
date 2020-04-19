import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
import django
django.setup()
from read import *
from players.models import *

def readPlayers():
# creates empty players dictionary
    players = {}

# calls all functions to fill in dictionaries
    players, QBs = ReadQB(players)
    players, RBs = ReadRB(players)
    players, WRs = ReadWR(players)
    players, TEs = ReadTE(players)
    players, Ks = ReadK(players)
    players, DEFs = ReadDEF(players)
    players, QBs = PosTiers("stats/QB_Tiers.txt", players, QBs, "QB")
    players, RBs = PosTiers("stats/RB_Tiers.txt", players, RBs, "RB")
    players, WRs = PosTiers("stats/WR_Tiers.txt", players, WRs, "WR")
    players, TEs = PosTiers("stats/TE_Tiers.txt", players, TEs, "TE")
    players, Ks = PosTiers("stats/K_Tiers.txt", players, Ks, "K")
    players, DEFs = DEFTiers(players, DEFs)
    players, QBs, RBs, WRs, TEs, Ks, DEFs = ReadTiers("stats/Tiers.txt", players, QBs, RBs, WRs, TEs, Ks, DEFs)


    # calculate composite for each player in each dict
    for player in players.values():
        if player.avgPosRank != 500 and player.avgRank != 500:
            player.composite = player.avgPosRank + player.avgRank + player.projRank + player.newPosRank + player.tier + player.posTier
            player.composite = round(player.composite, 3)

    for player in QBs.values():
        if player.avgPosRank != 500 and player.avgRank != 500:
            player.composite = player.avgPosRank + player.avgRank + player.projRank + player.newPosRank + player.tier + player.posTier
            player.composite = round(player.composite, 3)

    for player in RBs.values():
        if player.avgPosRank != 500 and player.avgRank != 500:
            player.composite = player.avgPosRank + player.avgRank + player.projRank + player.newPosRank + player.tier + player.posTier
            player.composite = round(player.composite, 3)

    for player in WRs.values():
        if player.avgPosRank != 500 and player.avgRank != 500:
            player.composite = player.avgPosRank + player.avgRank + player.projRank + player.newPosRank + player.tier + player.posTier
            player.composite = round(player.composite, 3)

    for player in TEs.values():
        if player.avgPosRank != 500 and player.avgRank != 500:
            player.composite = player.avgPosRank + player.avgRank + player.projRank + player.newPosRank + player.tier + player.posTier
            player.composite = round(player.composite, 3)

    for player in Ks.values():
        if player.avgPosRank != 500 and player.avgRank != 500:
            player.composite = player.avgPosRank + player.avgRank + player.projRank + player.newPosRank + player.tier + player.posTier
            player.composite = round(player.composite, 3)

    for player in DEFs.values():
        if player.avgPosRank != 500 and player.avgRank != 500:
            player.composite = player.avgPosRank + player.avgRank + player.projRank + player.newPosRank + player.tier + player.posTier
            player.composite = round(player.composite, 3)

    # put all players into new dictionaries
    # this acts essentially as a c++ multimap, storing all players
    # with keys as composite and vals as lists of players with that composite
    bestAll = defaultdict(list)
    bestQBs = defaultdict(list)
    bestRBs = defaultdict(list)
    bestWRs = defaultdict(list)
    bestTEs = defaultdict(list)
    bestKs = defaultdict(list)
    bestDEFs = defaultdict(list)

    for player in players.values():
        bestAll[player.composite].append(player)
    for player in QBs.values():
        bestQBs[player.composite].append(player)
    for player in RBs.values():
        bestRBs[player.composite].append(player)
    for player in WRs.values():
        bestWRs[player.composite].append(player)
    for player in TEs.values():
        bestTEs[player.composite].append(player)
    for player in Ks.values():
        bestKs[player.composite].append(player)
    for player in DEFs.values():
        bestDEFs[player.composite].append(player)

    bestAll = OrderedDict(sorted(bestAll.items()))
    bestQBs = OrderedDict(sorted(bestQBs.items()))
    bestRBs = OrderedDict(sorted(bestRBs.items()))
    bestWRs = OrderedDict(sorted(bestWRs.items()))
    bestTEs = OrderedDict(sorted(bestTEs.items()))
    bestKs = OrderedDict(sorted(bestKs.items()))
    bestDEFs = OrderedDict(sorted(bestDEFs.items()))

# some printing for testing purposes
    """
    for vals in bestQBs.values():
        for player in vals:
            if player.composite != 10000:
                print(str(player.composite) + ' ' + player.name + ' ' + str(player.projRank))
    """

    return bestQBs

def GetTeam(abbrev):
    #if it can't find the team it makes a new one
    try:
        t = Team.objects.get(team_short_name = abbrev)
    except Team.DoesNotExist:
        t = Team(team_short_name = abbrev)
        t.save()
    return t

def QBToWeb(player):
    #tries to find the player first, else it will create a new one
    try:
        p = Quarterback.objects.get(first_name = player.first_name, last_name = player.last_name)
    except Quarterback.DoesNotExist:
        p = Quarterback(first_name = player.first_name, last_name = player.last_name)
    p.team = GetTeam(player.proTeam)
    p.past_points = player.pastPoints
    p.past_PPG = player.pastPPG
    p.projected_rank = player.projRank
    p.games = player.games
    p.tier = player.tier
    p.pos_tier = player.posTier
    p.composite = player.composite
    p.completions = player.passComp
    p.attempts = player.passAtt
    p.yards = player.passYard
    p.touchdowns = player.passTD
    p.interceptions = player.passInt
    p.rushing_attempts = player.rushAtt
    p.rushing_yds = player.rushYard
    p.rushing_touchdowns = player.rushTD
    p.save()


#main execution
players = readPlayers()

for p in players:
    QBToWeb(players.get(p))
