import urllib
from bs4 import BeautifulSoup

#url = raw_input('Enter - ')
url = 'http://python-data.dr-chuck.net/known_by_Samiya.html'
count, pos = 7, 17
print url
for u in range(count):

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    url = tags[pos].get('href', None)
    print url