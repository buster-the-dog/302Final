import requests
import bs4
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re

# function that gets stats of players from 2019-2020
def PastStats(url, filename, position):
  
  filename = "stats/" + filename
  f = open(filename, "w")
  players = []
  mod = 0       #figures out modulus for printing purposes

  #goes to the website
  page = requests.get(url)

  #puts content into soup
  soup = BeautifulSoup(page.text, 'html.parser')

  #sorts through soup to find necessary info
  rows = (soup.find_all(class_='sort1'))

  for row in rows:
    for string in row.strings:
      players.append(string)
      
  # figure out what position it is for printing purposes
  if position == "QB" or position == "DEF":
    mod = 14
  elif position == "RB" or position == "WR":
    mod = 13
  elif position == "TE":
    mod = 10
  elif position == "K":
    mod = 11
  else:
    print("Bad Position")
    return -1
  
  count = 0
  for obj in players:
    if count % mod == 0:
      f.write('\n')
    
    f.write(obj + " ")
    count = count + 1


def FutureRankings(url, filename):

  #this opens the file
  filename = "stats/" + filename
  f = open(filename, "w")

  #this one can't use BS because the table is generated with javascript,
  #so requests_html is used instead to simulate an HTML session
  session = HTMLSession()
  r = session.get(url)
  r.html.render()

  # this creates a list of players
  players = [element.text for element in r.html.find('td a')]
  

  # empty strings are put into this list, so here I remove them
  realPlayers = []

  for player in players:
    if player != '':
      realPlayers.append(player)

  # write to file
  i = 1
  for player in realPlayers:
    f.write(player + ' ' + str(i) + '\n')
    i += 1

# function to get players in tiers
def FutureTiers(url, filename):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')

  filename = "stats/" + filename

  f = open(filename, "w")

  # this gets all the players names and what tier, prints to file
  rows = soup.find_all(class_=['full-name', 'tier-row static'])
  for row in rows:
    f.write(row.text)
    f.write('\n')

# will remain commented out until websites are fixed
"""
# program to get strength of schedule
def SoS(url, filename):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')

  filename = "stats/" + filename

  f = open(filename, "w")

  rows = soup.find_all(class_='c')
  for row in rows:
    print(row)
"""


# main begins here

# make function calls here
# first, QBs
PastStats("https://fftoday.com/stats/playerstats.php?Season=2019&GameWeek=&PosID=10", "QBs.txt", "QB")

# then RBs
PastStats("https://fftoday.com/stats/playerstats.php?Season=2019&GameWeek=&PosID=20&LeagueID=26955", "RBs.txt", "RB")

# now WRs
PastStats("https://fftoday.com/stats/playerstats.php?Season=2019&GameWeek=&PosID=30&LeagueID=26955", "WRs.txt", "WR")

# TEs
PastStats("https://fftoday.com/stats/playerstats.php?Season=2019&GameWeek=&PosID=40&LeagueID=26955", "TEs.txt", "TE")

# Ks
PastStats("https://fftoday.com/stats/playerstats.php?Season=2019&GameWeek=&PosID=80&LeagueID=26955", "Ks.txt", "K")

# DEFs
PastStats("https://fftoday.com/stats/playerstats.php?Season=2019&GameWeek=&PosID=99&LeagueID=26955", "DEFs.txt", "DEF")

# List of Players 1-311 in tiers
FutureTiers("https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php", "Tiers.txt")

# Basic list of players 1-311
FutureRankings("http://partners.fantasypros.com/external/widget/fp-widget.php?height=800px&width=100%25&thead_color=%23ffffff&thead_font=%23000000&t_alt_row=%23fafafa&link_color=%233778be&pill_color=%232881eb&sport=NFL&wtype=preseason&filters=&scoring=HALF&expert=769&affiliate_code=&year=2020&week=0&auction=false&Notes=false&tags=false&cards=true&format=table&promo_link=false&positions=QB%3ADST%3AK&ppr_positions=&half_positions=ALL%3ARB%3AWR%3ATE&site=&fd_aff=&dk_aff=&fa_aff=&dp_aff=&", "ranks.txt")

# Below will be strength of schedule websites, but they're currently broken
# so will be added later

# Calls Strength of Schedule for full season
# SoS("https://fftoolbox.fulltimefantasy.com/football/strength_of_schedule.cfm", "Sos_full.txt")