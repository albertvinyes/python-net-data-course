import re

f = open('file1.txt')
t = 0
for line in f:
    l = line.rstrip()
    numbers = re.findall('[0-9]+',l)
    for number in numbers:
        t += int(number)
print t
