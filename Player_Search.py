import re
import urllib2
from bs4 import BeautifulSoup
import json

__author__ = 'alast'

#file = open("fantasy.csv", "wb")
#1) Add Player's last name to Search URL, print search URL and then locate search results table
def player_search():
    global alink
    global final_alink
    global final_name
    global final_position_format
    player_last_name = raw_input("Enter last name: ")
    html_calc = "http://espn.go.com/nfl/players?search=" + player_last_name
    print (html_calc)
    html_final = urllib2.urlopen(html_calc)
    soup = BeautifulSoup(html_final, "lxml")
    table = soup.find("table",{"class": "tablehead"})

#2) Create empty list, loop through search results table and add all URL link's to empty list
    list = []
    for link in table.findAll('a', href=re.compile(player_last_name)):
        alink = link.get('href')
        list.append(alink)
    #If there is only one player with the search criteria used, run the function that displays the players data
    #if len(list) == 1:
    #player_data(list)
    count = 0
    #Instead of a list create a dict where the final_name is the key and the other variables are the values
    multi_player_list = []
    if len(alink) == 1:
        player_page = urllib2.urlopen(alink)
        player_soup = BeautifulSoup(player_page, "lxml")
        search_name = player_soup.find("div", {"class": "mod-content"}).h1
        search_position = player_soup.findAll("li", {"class": "first"}, limit=1)
        final_name = search_name.text
        final_position = search_position[0].text
        #exclude whitespace
        final_position_format = final_position[3:].strip()
        print final_name
        print final_position_format
        print alink
    else:
        for alink in list:
            count += 1
            player_page = urllib2.urlopen(alink)
            player_soup = BeautifulSoup(player_page, "lxml")
            search_name = player_soup.find("div", {"class": "mod-content"}).h1
            final_name = search_name.text
            search_position = player_soup.findAll("li", {"class": "first"}, limit=1)
            final_position = search_position[0].text
            #exclude player number and whitespace
            final_position_format = final_position[3:].strip()
            multi_player_list.append(final_name)
            multi_player_list.append(alink)
            print count
            print final_name
            print final_position_format
            print alink

#run function until user selects a number in the list
#def choose_player():
    player_list_number = int(raw_input("Type in the number of the player you want: "))
    if player_list_number > count:
        print "The list only goes up to " + str(count)
    elif player_list_number <1:
        print "No player has this number. The list goes from 1 to " + str(count)
    else:
        final_alink = list[player_list_number-1]
        return final_alink
        return final_name
        return final_position_format

player_search()
#choose_player()