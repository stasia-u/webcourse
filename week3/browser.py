import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.data.pr4e.org', 80))

mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data
mysock.close()
# import urllib
#
# fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
#
# counts = dict()
# for line in fhand:
#     print line.strip()
#     words = line.split()
#     for word in words:
#         counts[word]=counts.get(word,0) + 1
# print counts
