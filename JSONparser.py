import json
import urllib

url = raw_input('URL:')
data = urllib.urlopen(url).read();
comments = json.loads(data)['comments']

t = 0
for comment in comments:
    t += int(comment['count'])
print t
