import urllib
from bs4 import BeautifulSoup

#url = raw_input ('Enter - ')
url = 'http://python-data.dr-chuck.net/comments_318092.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
Sum, Count = 0, 0

for tag in tags:
    Sum += int(tag.contents[0])
    Count += 1
print "Count ", Count
print "Sum ", Sum