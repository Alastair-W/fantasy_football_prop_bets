__author__ = 'alastair'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import BeautifulSoup

browser = webdriver.Firefox()
browser.get('http://espn.go.com/nfl/player/_/id/11467/justin-forsett')
html_source = browser.page_source
browser.quit()

only_fantasy_stats = SoupStrainer("fantasy-stats")

soup = BeautifulSoup.BeautifulSoup(html_source)
fantasy = soup.find(id="fantasy-stats")
print (fantasy.ul.prettify())
