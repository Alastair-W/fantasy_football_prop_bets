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



def find_player_data():
    html_final = urllib2.urlopen(reco_html)
    soup = BeautifulSoup(html_final)
    player_data_list = []
    for section in soup.find(class_ = {"evenrow", "oddrow"}):
        player_data_list.append(section)
        #only return the relevant information for the players selected in the Player Recommendation file
        #use a counter to establish which number correlates to which player
        #display the right data and then loop through the other players recommended
    print player_data_list[0:7]


find_player_data()