# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
count = int(input('Enter Count: '))
position = int(input('Enter Position: ')) - 1
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
names = []
# Loop runs according to the count set
for tag in range(count):
    link = tags[position].get('href', None)
    # print(tags[position].contents[0])
    names.append(tags[position].contents[0])
    # Recursive 
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

print(names[-1])


# http://py4e-data.dr-chuck.net/known_by_Fikret.html