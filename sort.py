# here are all of the class definitions
class Player:
    def __init__(self):
        self.name = ""
        self.pastPoints = 0.0
        self.pastPPG = 0.0
        self.projRank = 0
        self.proTeam = ""
        self.games = 0
        self.tier = 0
    
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
        self.FG% = 0.0
        self.EPM = 0
        self.EPA = 0

class Defense(Player):
    def __init__self():
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