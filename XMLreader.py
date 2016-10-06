import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_182328.xml'
data = urllib.urlopen(url).read()

tree = ET.fromstring(data)
counts = tree.findall('.//count')

s = 0
for count in counts:
    n = int(count.text)
    s += n
print s
