import urllib
import xml.etree.ElementTree as ET

while True:
    my_url = raw_input('Enter location: ')
    if len(my_url) < 1 : break

    print 'Retrieving', my_url
    uh = urllib.urlopen(my_url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)
    stuff = tree.findall('comments/comment')
    Sum = 0
    for item in stuff:
        Sum += int(item.find('count').text)

    print 'Count: ', len(stuff)
    print 'Sum: ', Sum