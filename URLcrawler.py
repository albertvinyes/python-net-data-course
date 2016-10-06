import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter URL:')
count = int(raw_input('Enter count:'))
position = int(raw_input('Enter position:'))-1
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
print "Retrieving:", url

while count > 0:
    name = tags[position].contents[0]
    href = str(tags[position].get('href', None))
    html = urllib.urlopen(href).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print "URL:", href, "- Name:", name
    count -= 1
    
