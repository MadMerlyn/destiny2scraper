# -*- coding: utf-8 -*-
"""
Destiny2 Weekly Reset Scraper
@author: MadMerlyn
"""

from urllib.request import urlopen
import sys
from bs4 import BeautifulSoup as web

#Load LiveEvents submenu
ORIGINAL = sys.stdout
HTML = urlopen('https://www.bungie.net/en/Explore/Category?category=LiveEvents')
SOUP = web(HTML, 'lxml')
#Grab all event links and crawl them
LINKS = SOUP.find_all('a', {'class':'explore-item'})
CRAWL = ['https://www.bungie.net'+x.get('href') for x in LINKS]
HTML2 = [urlopen(x) for x in CRAWL]
ACTIVITIES = [web(x, 'lxml') for x in HTML2]

for item in ACTIVITIES:
    act = item.find('div', {'id':'explore-container'})
    if 'nightfall' in act.get_text().lower():
        event_dates = act.find('div', {'destiny-event-date-range'}).get_text().strip()
        div = act.find('div', {'data-identifier':'quest-activity-information'})
        title = div.find('div', {'class':'title'}).get_text()
        subtitle = div.find('div', {'class':'subtitle'}).get_text()
        div = act.findAll('div', {'data-identifier':'modifier-information'})
        mods = [x.find('div', {'class':'title'}).get_text() for x in div]
        mod_descs = [x.find('div', {'class':'subtitle'}).get_text() for x in div]

        print(title+'  ('+event_dates+')', subtitle, sep='\n', end='\n\n')
        print('Modifiers:')
        for i, (mod, desc) in enumerate(zip(mods, mod_descs)):
            print('    '+mod, '       '+desc+'\n', sep='\n', end='\n')

    else:
        div = act.find('div', {'data-identifier':'quest-information'})
        title = div.find('div', {'class':'title'}).get_text()

        print(title+'  ('+event_dates+')', sep='\n', end='\n\n')
