import re
import urllib2
from bs4 import BeautifulSoup
import json

__author__ = 'alast'

#file = open("fantasy.csv", "wb")
#1) Search for player

player_last_name = raw_input("Enter last name: ")
html_calc = "http://espn.go.com/nfl/players?search=" + player_last_name
print (html_calc)
html_final = urllib2.urlopen(html_calc)
soup = BeautifulSoup(html_final)
table = soup.find("table",{"class": "tablehead"})

list = []
for link in table.findAll('a', href=re.compile(player_last_name)):
    #print(link.get('href'))
    alink = link.get('href')
    #print alink
    list.append(alink)

#if len(list) == 1;
#    player_data()
#else:
    print list

#print len(list)
#print alink.list

#2a) if list of players only has one link, one for the link of each player returned from the search query, then open page


#2b) if table has more than one row display table and ask user to select

#3) User selects player to return html like below
#html = urllib.urlopen('http://espn.go.com/nfl/player/_/id/11467/justin-forsett')

#4) If player is correct, write to 'Pairs' table new with 'Pair x', 'Date' ,'User 1',the player as 'Player 1'
# then loop through same process for 'Player 2' and 'User 2'

#4a) Player 1 Recommendation: User can either choose a position or select any, then app will randomly choose a position and then
#choose one player in the top 32 rankings.

#4b) Player 2 Recommendation: Pivoting off the first player, the user will be given a list of 4 players - 2 above and
#2 below

#4c) Pair Recommendation: User can either choose a position or select any, then app will randomly choose a position and then
#choose one player in the top 32 rankings followed by a second player randomly from 2 places above or below

#5) Display 'Pairs' associated with User

#6) Return fantasy data from web page for all players in 'Pairs' table

def player_data():
    soup = BeautifulSoup(r.text)
    search_tag = soup.findAll(id='my-players-table')
    search_tag_format = str
    tag = soup.findAll(id='fantasy-content')
#tag_string = str(tag)
#raw_string = tag.get_text()
#string = json.loads(raw_string)
#print(string['fullName'])
#print(string['pointsSEASON'])
    tag_format = str(tag)
    tag_list = tag_format.split(":")
    name = tag_list[10]
    averagePoints = tag_list[1]
    totalPoints = tag_list[18]
    name_list = name.split(",")
    averagePoints_list = averagePoints.split(",")
    totalPoints_list = totalPoints.split("}")
    averagePoints_final = averagePoints_list[0]
    totalPoints_final = totalPoints_list[0]

#print len(tag_list)
#print tag
print ("Player Name: " + name_list[0])
print ("Average Points: " + averagePoints_final)
print ("Total Points: " + totalPoints_final)
#print str(tag.split(":", 1))



#wr = csv.writer(file, delimiter=',')
#wr.writerow(tag)