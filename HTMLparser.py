import urllib
import re
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_182331.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

total = 0
tags = soup('span')
for tag in tags:
    total += int(re.findall('[0-9]+',str(tag.contents[0]))[0])

print total
