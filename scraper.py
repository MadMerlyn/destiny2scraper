# -*- coding: utf-8 -*-
"""
Destiny2 Weekly Reset Scraper
@author: MadMerlyn
"""

from urllib.request import urlopen
import sys
import re
from bs4 import BeautifulSoup as web

ORIGINAL = sys.stdout
HTML = urlopen('https://www.bungie.net/en/Explore/Category?category=LiveEvents')
SOUP = web(HTML, 'lxml')

LINKS = SOUP.find_all('a', {'class':'explore-item'})
CRAWL = ['https://www.bungie.net'+x.get('href') for x in LINKS]
ACTIVITIES = [urlopen(x) for x in CRAWL]



test = web(ACTIVITIES[0], 'lxml')
result = test.find_all('div', {'class':'title'})

for item in result:
    if 'nightfall' in item.get_text().lower():
        print(item.get_text())
