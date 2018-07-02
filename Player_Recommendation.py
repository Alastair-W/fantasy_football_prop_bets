import re
import urllib2
from bs4 import BeautifulSoup
import json

__author__ = 'alast'

player_one = "Julio Jones"
final_position_format = "WR"
reco_html = "null"

def recommendation_page():
    global reco_html
    if final_position_format == "WR":
        reco_html = "http://espn.go.com/nfl/statistics/player/_/stat/receiving"
    elif final_position_format == "QB":
        reco_html = "http://espn.go.com/nfl/statistics/player/_/stat/passing"
    elif final_position_format == "TE":
        reco_html = "http://espn.go.com/nfl/statistics/player/_/stat/receiving"
    elif final_position_format == "RB":
        reco_html = "http://espn.go.com/nfl/statistics/player/_/stat/rushing"
    elif final_position_format == "PK":
        reco_html = "http://espn.go.com/nfl/statistics/player/_/stat/kicking"
    return reco_html

recommendation_page()
print reco_html



def find_players():
    global previous_players
    global next_players
    html_final = urllib2.urlopen(reco_html)
    soup = BeautifulSoup(html_final, "lxml")
    table = soup.find("table",{"class": "tablehead"})

#NEW OPTION define a function that takes the following arguments
#Siblings of Tag that is table class = tablehead,tr class oddrow or even row, a href
#Siblings logic is below

    player_name = table.find("a",text = player_one)
    player_row = player_name.find_parent("tr")
    player_number_code = player_row.find("td")
    player_number = int(player_number_code.get_text())

    print player_row
    print soup.table.find_all('a')
#Create function that finds player recommendations based on the number of the initial player
#If the number is 1 show 0 lower and 4 higher
#If the number is 2 show 1 lower and 3 higher
#If number is 11, 21 or 31 skip the row directly above as there are headers every 10 rows
#If number is 39 show 3 lower and 1 higher
#If the number is 40 show 4 lower and 0 higher

    if player_number == 1:
        next_players = player_row.find_next_siblings("tr", limit = 4)
        print next_players
        #Need to find a way to split the variable based on the '>' character and then only return the 5th item - which
        #contains the html address for the player. Then i can just follow the same Player Data Function.py
    elif player_number == 2:
        next_players = player_row.find_next_siblings("tr", limit=3)
        previous_players = player_row.previous_sibling
        print next_players
        print previous_players
    elif player_number == 11 or 21 or 31:
        next_players = player_row.find_next_siblings("tr", limit=2)
        previous_players = player_row.find_previous_siblings("tr", limit=3)
        print next_players
        #next line doesn't print the tr class = colhead row as this does not contain player data
        print previous_players[1:3]
    elif player_number == 39:
        next_players = player_row.find_next_siblings("tr", limit=3)
        previous_players = player_row.find_previous_siblings("tr", limit=1)
        print next_players
        print previous_players
    elif player_number == 40:
        previous_players = player_row.find_previous_siblings("tr", limit=4)
        print previous_players
    else:
        next_players = player_row.find_next_siblings("tr", limit=2)
        previous_players = player_row.find_previous_siblings("tr", limit=2)
        print next_players
        print previous_players

find_players()

#print Name & Position, Team, Points, Receptions, Targets, Yards & TDs
#def show_player_stats():

#show_player_stats()