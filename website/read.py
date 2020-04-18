from collections import OrderedDict     # to sort by key
from collections import defaultdict     # to easily make a dictionary of lists

# here are all of the class definitions
class Player:
    def __init__(self):
        self.name = ""
        self.first_name = ""
        self.last_name = ""
        self.pastPoints = 0.0
        self.pastPPG = 0.0
        self.projRank = 500
        self.proTeam = ""
        self.games = 0
        self.tier = 0
        self.posTier = 0
        self.position = ""
        self.pastPosRank = 0
        self.newPosRank = 500
        self.avgRank = 500
        self.avgPosRank = 500
        self.composite = 10000.0    # this is the money number that figures out a player's actual value
    
# all position classes are inherited from player so they have all the values in the player class
class QB(Player):
    def __init__(self):
        super().__init__()
        self.passComp = 0
        self.passAtt = 0
        self.passYard = 0
        self.passTD = 0
        self.passInt = 0
        self.rushAtt = 0
        self.rushYard = 0
        self.rushTD = 0

class RB(Player):
    def __init__(self):
        super().__init__()
        self.rushAtt = 0
        self.rushYard = 0
        self.rushTD = 0
        self.recTarget = 0
        self.receptions = 0
        self.recYard = 0
        self.recTD = 0

class WR(Player):
    def __init__(self):
        super().__init__()
        self.recTarget = 0
        self.receptions = 0
        self.recYard = 0
        self.recTD = 0
        self.rushAtt = 0
        self.rushYard = 0
        self.rushTD = 0

class TE(Player):
    def __init__(self):
        super().__init__()
        self.recTarget = 0
        self.receptions = 0
        self.recYard = 0
        self.recTD = 0

class K(Player):
    def __init__(self):
        super().__init__()
        self.FGM = 0
        self.FGA = 0
        self.FGpercent = 0.0
        self.EPM = 0
        self.EPA = 0

class Defense(Player):
    def __init__(self):
        super().__init__()
        self.games = 16
        self.sack = 0
        self.FR = 0
        self.intercept = 0
        self.TD = 0
        self.PA = 0
        self.passYPG = 0.0
        self.rushYPG = 0.0
        self.safety = 0
        self.kickTD = 0

# this global dict is a look up table to get the abbreviations for defenses, which
# are given in one website as the team's entire name, so that a team's abbr. is always its name
teams = {
    '49ers' : 'SF',
    'Steelers' : 'PIT',
    'Ravens' : 'BAL',
    'Bills' : 'BUF',
    'Patriots' : 'NE',
    'Rams' : 'LAR',
    'Bears' : 'CHI',
    'Chiefs' : 'KC',
    'Vikings' : 'MIN',
    'Saints' : 'NO',
    'Chargers' : 'LAC',
    'Broncos' : 'DEN',
    'Jets' : 'NYJ',
    'Eagles' : 'PHI',
    'Seahawks' : 'SEA',
    'Titans' : 'TEN',
    'Packers' : 'GB',
    'Cowboys' : 'DAL',
    'Colts' : 'IND',
    'Buccaneers' : 'TB',
    'Browns' : 'CLE',
    'Texans' : 'HOU',
    'Jaguars' : 'JAC',
    'Falcons' : 'ATL',
    'Redskins' : 'WAS',
    'Panthers' : 'CAR',
    'Lions' : 'DET',
    'Raiders' : 'LV',
    'Giants' : 'NYG',
    'Dolphins' : 'MIA',
    'Cardinals' : 'ARI',
    'Bengals' : 'CIN'
}

# this function reads QBs.txt and sorts stats from 2019-2020 Quarterbacks
def ReadQB(players):
    f = open("stats/QBs.txt", "r")

    words = []
    QBs = {}

    # run through the file to pull data
    for line in f:
        words.clear()
        words = line.split()
        if len(words) != 0:

            # create a new Player and fill in relevant data
            p = Player()

            p.position = "QB"
            p.pastPosRank = words[0]
            
            # special case here since some player names are long
            if(len(words) == 16):
                p.name = words[1] + ' ' + words[2] + ' ' + words[3]
                
                # this deletes a value so the rest of the read can go normally
                del words[3]
            else:
                p.name = words[1] + ' ' + words[2]

            nameSplit = p.name.split()

            p.first_name = nameSplit[0]
            if(len(nameSplit) == 3):
                p.last_name = nameSplit[1] + ' ' + nameSplit[2]
            else:
                p.last_name = nameSplit[1]


            p.proTeam = words[3]
            p.games = words[4]
            p.pastPoints = words[13]
            p.pastPPG = words[14]

            players[p.name] = p
            
            q = QB()

            # this statement initializes all the values shared by q and p with values in p
            #q.__dict__ = p.__dict__

            q.pastPosRank = p.pastPosRank
            q.position = "QB"
            q.name = p.name
            q.first_name = p.first_name
            q.last_name = p.last_name
            q.proTeam = p.proTeam
            q.games = p.games
            q.pastPoints = p.pastPoints
            q.pastPPG = p.pastPPG
            q.passComp = words[5]
            q.passAtt = words[6]
            q.passYard = int(words[7].replace(',', ''))
            q.passTD = words[8]
            q.passInt = words[9]
            q.rushAtt = words[10]
            q.rushYard = int(words[11].replace(',', ''))
            q.rushTD = words[12]

            QBs[q.name] = q

    f.close()
    return players, QBs

# This function behaves similarly to ReadQB, except for RBs
def ReadRB(players):
    f = open("stats/RBs.txt", "r")

    words = []
    RBs = {}

    # iterate through the file
    for line in f:
        words.clear()
        words = line.split()
        if(len(words) != 0):
            p = Player()
            
            p.position = "RB"
            p.pastPosRank = words[0]
            
            # special case here since some player names are long
            if(len(words) == 15):
                p.name = words[1] + ' ' + words[2] + ' ' + words[3]
                
                # this deletes a value so the rest of the read can go normally
                del words[3]
            else:
                p.name = words[1] + ' ' + words[2]
            
            nameSplit = p.name.split()

            p.first_name = nameSplit[0]
            if(len(nameSplit) == 3):
                p.last_name = nameSplit[1] + ' ' + nameSplit[2]
            else:
                p.last_name = nameSplit[1]

            p.proTeam = words[3]
            p.games = words[4]
            p.pastPoints = words[12]
            p.pastPPG = words[13]

            players[p.name] = p


            r = RB()
            
            # initialize r with all of p's values
            #r.__dict__ = p.__dict__

            r.pastPosRank = p.pastPosRank
            r.position = "RB"
            r.name = p.name
            r.first_name = p.first_name
            r.last_name = p.last_name
            r.proTeam = p.proTeam
            r.games = p.games
            r.pastPoints = p.pastPoints
            r.pastPPG = p.pastPPG
            r.rushAtt = words[5]
            r.rushYard = words[6]
            r.rushTD = words[7]
            r.recTarget = words[8]
            r.receptions = words[9]
            r.recYard = words[10]
            r.recTD = words[11]

            RBs[r.name] = r

    f.close()
    return players, RBs

# same as above, but with WRs
def ReadWR(players):
    f = open("stats/WRs.txt", 'r')
    
    words = []
    WRs = {}

    for line in f:
        words.clear()
        words = line.split()
        
        if(len(words) != 0):
            p = Player()

            p.position = "WR"
            p.pastPosRank = words[0]

            # special case here since some player names are long
            if(len(words) == 15):
                p.name = words[1] + ' ' + words[2] + ' ' + words[3]
                
                # this deletes a value so the rest of the read can go normally
                del words[3]
            else:
                p.name = words[1] + ' ' + words[2]

            nameSplit = p.name.split()

            p.first_name = nameSplit[0]
            if(len(nameSplit) == 3):
                p.last_name = nameSplit[1] + ' ' + nameSplit[2]
            else:
                p.last_name = nameSplit[1]

            p.proTeam = words[3]
            p.games = words[4]
            p.pastPoints = words[12]
            p.pastPPG = words[13]

            players[p.name] = p


            wr = WR()
            #wr.__dict__ = p.__dict__

            wr.pastPosRank = p.pastPosRank
            wr.position = "QB"
            wr.name = p.name
            wr.first_name = p.first_name
            wr.last_name = p.last_name
            wr.proTeam = p.proTeam
            wr.games = p.games
            wr.pastPoints = p.pastPoints
            wr.pastPPG = p.pastPPG
            wr.recTarget = words[5]
            wr.receptions = words[6]
            wr.recYard = words[7]
            wr.recTD = words[8]
            wr.rushAtt = words[9]
            wr.rushYard = words[10]
            wr.rushTD = words[11]

            WRs[wr.name] = wr

    f.close()
    return players, WRs

# same as above
def ReadTE(players):
    f = open("stats/TEs.txt", 'r')

    words = []
    TEs = {}

    for line in f:
        words.clear()
        words = line.split()
        if(len(words) != 0):
            p = Player()

            p.position = "TE"
            p.pastPosRank = words[0]
            
            # special case here since some player names are long
            if(len(words) == 12):
                p.name = words[1] + ' ' + words[2] + ' ' + words[3]
                
                # this deletes a value so the rest of the read can go normally
                del words[3]
            else:
                p.name = words[1] + ' ' + words[2]

            nameSplit = p.name.split()

            p.first_name = nameSplit[0]
            if(len(nameSplit) == 3):
                p.last_name = nameSplit[1] + ' ' + nameSplit[2]
            else:
                p.last_name = nameSplit[1]
                
            p.proTeam = words[3]
            p.games = words[4]
            p.pastPoints = words[9]
            p.pastPPG = words[10]

            players[p.name] = p


            te = TE()
            #te.__dict__ = p.__dict__

            te.pastPosRank = p.pastPosRank
            te.position = "QB"
            te.name = p.name
            te.first_name = p.first_name
            te.last_name = p.last_name
            te.proTeam = p.proTeam
            te.games = p.games
            te.pastPoints = p.pastPoints
            te.pastPPG = p.pastPPG
            te.recTarget = words[5]
            te.receptions = words[6]
            te.recYard = words[7]
            te.recTD = words[8]

            TEs[te.name] = te
    
    f.close()
    return players, TEs

# same as above
def ReadK(players):
    f = open("stats/Ks.txt", 'r')

    words = []
    Ks = {}

    for line in f:
        words.clear()
        words = line.split()
        if(len(words) != 0):
            p = Player()

            p.position = "K"
            p.pastPosRank = words[0]
            
            # special case here since some player names are long
            if(len(words) == 13):
                p.name = words[1] + ' ' + words[2] + ' ' + words[3]
                
                # this deletes a value so the rest of the read can go normally
                del words[3]
            else:
                p.name = words[1] + ' ' + words[2]
            
            nameSplit = p.name.split()

            p.first_name = nameSplit[0]
            if(len(nameSplit) == 3):
                p.last_name = nameSplit[1] + ' ' + nameSplit[2]
            else:
                p.last_name = nameSplit[1]

            p.team = words[3]
            p.games = words[4]
            p.pastPoints = words[10]
            p.pastPPG = words[11]

            players[p.name] = p


            k = K()
            #k.__dict__ = p.__dict__

            k.pastPosRank = p.pastPosRank
            k.position = "QB"
            k.name = p.name
            k.first_name = p.first_name
            k.last_name = p.last_name
            k.proTeam = p.proTeam
            k.games = p.games
            k.pastPoints = p.pastPoints
            k.pastPPG = p.pastPPG
            k.FGM = words[5]
            k.FGA = words[6]
            k.FGpercent = words[7]
            k.EPM = words[8]
            k.EPA = words[9]

            Ks[k.name] = k

    f.close()
    return players, Ks

#same as above
def ReadDEF(players):
    f = open("stats/DEFs.txt", 'r')

    words = []
    DEFs = {}

    for line in f:
        words.clear()
        words = line.split()
        if(len(words) != 0):
            p = Player()

            p.position = "DEF"
            p.pastPosRank = words[0]

            # special case here since some teams names are long
            if(len(words) == 16):
                name = words[1] + ' ' + words[2] + ' ' + words[3]
                
                # this deletes a value so the rest of the read can go normally
                del words[3]
            else:
                name = words[1] + ' ' + words[2]
            
            # here we access the look up table declared to get the abbreviation
            name = name.split()
            name = teams[name[len(name)-1]]

            p.name = name
            p.games = words[3]
            p.pastPoints = words[13]
            p.pastPPG = words[14]

            players[p.name] = p


            d = Defense()
            #d.__dict__ = p.__dict__

            d.pastPosRank = p.pastPosRank
            d.position = "QB"
            d.name = p.name
            d.first_name = p.first_name
            d.last_name = p.last_name
            d.proTeam = p.proTeam
            d.games = p.games
            d.pastPoints = p.pastPoints
            d.pastPPG = p.pastPPG
            d.sack = words[4]
            d.FR = words[5]
            d.intercept = words[6]
            d.TD = words[7]
            d.PA = words[8]
            d.passYPG = words[9]
            d.rushYPG = words[10]
            d.safety = words[11]
            d.kickTD = words[12]

            DEFs[d.name] = d
    
    f.close()
    return players, DEFs


# this function figures out what tier the player is in by position
# as well as the players rank compared to others at his position
def PosTiers(filename, players, posdict, position):
    f = open(filename, 'r')

    words = []

    for line in f:
        words = line.split()

        # handles blank line cases
        if len(words) == 0:
            pass

        # a line with just "tier x" in it indicates a new tier, this assigns it and moves on
        elif 'Tier' in line:
            tier = int(words[1])
        
        # if this else block occurs, the line is an actual player
        else:
            # assign avg
            avg = float(words[0])
            # assign rank
            rank = int(words[1])
            
            # assign name
            if len(words) == 6:
                name = words[2] + ' ' + words[3] + ' ' + words[4]
            else:
                name = words[2] + ' ' + words[3]

            # see if player is in dict already
            if name in players:
                players[name].newPosRank = rank
                players[name].posTier = tier
                players[name].avgPosRank = avg
                
                # checks position specific dict
                if name in posdict:
                    posdict[name].newPosRank = rank
                    posdict[name].posTier = tier
                    posdict[name].avgPosRank = avg
            
            # try removing suffix
            elif len(name.split()) == 3:
                split = name.split()
                name = split[0] + ' ' + split[1]
                if name in players:
                    players[name].newPosRank = rank
                    players[name].posTier = tier
                    players[name].avgPosRank = avg
                if name in posdict:
                    posdict[name].newPosRank = rank
                    posdict[name].posTier = tier
                    posdict[name].avgPosRank = avg

            # try removing punctuation
            elif '.' in name:
                for char in name:
                    if char == '.':
                        name = name.replace(char, '')
                if name in players:
                    players[name].newPosRank = rank
                    players[name].posTier = tier
                    players[name].avgPosRank = avg
                if name in posdict:
                    posdict[name].newPosRank = rank
                    posdict[name].posTier = tier
                    posdict[name].avgPosRank = avg


            # annoying case for Mitchell Trubisky
            # one website calls him "Mitch" instead of Mitchell
            elif 'Mitch' in name:
                name = "Mitchell Trubisky"
                if name in players:
                    players[name].newPosRank = rank
                    players[name].posTier = tier
                    players[name].avgPosRank = avg
                if name in posdict:
                    posdict[name].newPosRank = rank
                    posdict[name].posTier = tier
                    posdict[name].avgPosRank = avg
            
            # nothing worked, so create a new player
            else:
                p = Player()
                p.name = name
                p.position = position
                p.newPosRank = rank
                p.posTier = tier
                p.proTeam = words[len(words)-1]
                p.avgPosRank = avg
                players[p.name] = p

                if position == 'QB':
                    player = QB()
                elif position == 'RB':
                    player = RB()
                elif position == 'WR':
                    player = WR()
                elif position == 'TE':
                    player = TE()
                else:
                    player = K()
                
                #player.__dict__ = p.__dict__
                player.name = name
                player.position = position
                player.newPosRank = rank
                player.posTier = tier
                player.proTeam = words[len(words)-1]
                player.avgPosRank = avg
                posdict[player.name] = player
            
    f.close()
    return players, posdict
            
# made Def tiers a separate function because it would make the above function too clunky
def DEFTiers(players, DEFs):
    f = open("stats/DEF_Tiers.txt", 'r')

    words = []

    for line in f:
        words = line.split()

        # handles empty line
        if len(words) == 0:
            pass
        
        # handles line that indicates a new tier
        elif 'Tier' in line:
            tier = int(words[1])
        
        # handles player line
        else:
            avg = float(words[0])
            rank = int(words[1])
            name = words[len(words)-1]

            # Defenses name on this website look like (SF),
            # so we take out the parantheses to get the abbr.
            name = name.replace('(', '')
            name = name.replace(')', '')
            
            players[name].newPosRank = rank
            players[name].proTeam = name
            players[name].posTier = tier
            players[name].avgPosRank = avg

            DEFs[name].newPosRank = rank
            DEFs[name].proTeam = name
            DEFs[name].posTier = tier
            DEFs[name].avgPosRank = avg

    f.close()
    return players, DEFs

# Reads in the overall Tier of all players
def ReadTiers(filename, players, QBs, RBs, WRs, TEs, Ks, DEFs):
    f = open(filename, 'r')

    words = []

    for line in f:
        words = line.split()

        # handles empty lines
        if len(words) == 0:
            pass
        
        # handles new Tier
        elif 'Tier' in words:
            tier = int(words[1])
        
        # handles player info
        else:
            avg = float(words[0])
            rank = int(words[1])
            team = words[len(words)-1]

            # figure out name length
            # the ( ) case is for defenses
            if '(' in line:
                name = words[len(words)-1]
            elif len(words) == 6:
                name = words[2] + ' ' + words[3] + ' ' + words[4]
                del words[4]
            else:
                name = words[2] + ' ' + words[3]
            
            # get rid of ( ) in defenses name
            if '(' in name:
                name = name.replace('(', '')
                name = name.replace(')', '')
                team = name

            # see if player is in dict already
            if name in players:
                players[name].projRank = rank
                players[name].tier = tier
                players[name].avgRank = avg
                players[name].proTeam = team
            
            # try removing suffix
            elif len(name.split()) == 3:
                split = name.split()
                name = split[0] + split[1]
                if name in players:
                    players[name].projRank = rank
                    players[name].tier = tier
                    players[name].avgRank = avg
                    players[name].proTeam = team

            # try removing punctuation
            elif '.' in name:
                for char in name:
                    if char == '.':
                        name = name.replace(char, '')
                if name in players:
                    players[name].projRank = rank
                    players[name].tier = tier
                    players[name].avgRank = avg
                    players[name].proTeam = team


            # annoying case for mitchell Trubisky
            elif 'Mitch' in name:
                name = "Mitchell Trubisky"
                if name in players:
                    players[name].projRank = rank
                    players[name].tier = tier
                    players[name].avgRank = avg
                    players[name].proTeam = team
            
            # nothing worked
            else:
                p = Player()
                p.name = name
                p.projRank = rank
                p.tier = tier
                p.avgRank = avg
                p.proTeam = team
                players[p.name] = p
                


            # at this point, name is either correct or it's not worth
            # creating a specific position as it won't have most data
            if name in QBs:
                QBs[name].projRank = rank
                QBs[name].tier = tier
                QBs[name].avgRank = avg
                QBs[name].proTeam = team
            elif name in RBs:
                RBs[name].projRank = rank
                RBs[name].tier = tier
                RBs[name].avgRank = avg
                RBs[name].proTeam = team
            elif name in WRs:
                WRs[name].projRank = rank
                WRs[name].tier = tier
                WRs[name].avgRank = avg
                WRs[name].proTeam = team
            elif name in TEs:
                TEs[name].projRank = rank
                TEs[name].tier = tier
                TEs[name].avgRank = avg
                TEs[name].proTeam = team
            elif name in  DEFs:
                DEFs[name].projRank = rank
                DEFs[name].tier = tier
                DEFs[name].avgRank = avg
                DEFs[name].proTeam = team
            elif name in Ks:
                Ks[name].projRank = rank
                Ks[name].tier = tier
                Ks[name].avgRank = avg
                Ks[name].proTeam = team

    f.close()
    return players, QBs, RBs, WRs, TEs, Ks, DEFs
