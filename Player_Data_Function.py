import Player_Search
import urllib2
from bs4 import BeautifulSoup


__author__ = 'alast'

global final_alink
global final_name
global final_position_format

def player_data():
    #alink = 'http://espn.go.com/nfl/player/_/id/16733/odell-beckham-jr.'
    #web_page = urllib2.urlopen(alink)
    web_page = urllib2.urlopen(Player_Search.final_alink)
    soup = BeautifulSoup(web_page, "lxml")
    tag = soup.findAll(id='fantasy-content')
    tag_format = str(tag)
    tag_list = tag_format.split(":")
    print tag_list

    #fullName_index = [i for i, s in enumerate(tag_list) if "fullName" in s]
    #name_index = fullName_index[0] + 1
    #name = tag_list[name_index]
    #name_format = name.split('"')
    #create new variable that equals the list position below
    #print "Name: " + name_format[1]
    print "Name: " + final_name
    print "Position: " + final_position_format

    #Create formatted variable showing position that can be used in the Player_Recommendation function
    averagePoints_index = [i for i, s in enumerate(tag_list) if "averagePoints" in s]
    average_index = averagePoints_index[0] + 1
    average_points = tag_list[average_index]
    average_points_split = average_points.split('"')
    average_points_slice = average_points_split[0]
    average_points_format = average_points_slice[:-1]
    print "Average Points: " + average_points_format

    totalPoints_index = [i for i, s in enumerate(tag_list) if "totalPoints" in s]
    total_index = totalPoints_index[0] + 1
    total_points = tag_list[total_index]
    total_points_split = total_points.split('"')
    total_points_slice = total_points_split[0]
    total_index_plus = total_index + 1
    if total_index_plus == len(tag_list):
        total_points_format = total_points_slice[:-8]
    else:
        total_points_format = total_points_slice[:-1]
    print "Total Points: " + total_points_format


#player_data()