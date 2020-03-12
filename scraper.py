import requests
import bs4
from bs4 import BeautifulSoup

players = []

url = 'https://fftoday.com/stats/playerstats.php?Season=2019&GameWeek=&PosID=10'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

rows = (soup.find_all(class_='sort1'))

for row in rows:
# print(row.prettify())
# print(row.contents)
  for string in row.strings:
    players.append(string)
    
count = 0
for obj in players:
  if count % 14 == 0:
    print('\n')
  
  print(obj, end = ' ')
  count = count + 1