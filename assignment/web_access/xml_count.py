import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from lxml import etree
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter Url: ')
    html = urllib.request.urlopen(url, context=ctx)
    data = html.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)
    user = tree.findall('comments/comment')
    print('Count:', len(user))
    digits = []
    for item in user: 
    #     print('Name: ', item.find('name').text)
    #     print('Number:',item.find('count').text)
        digits.append(int(item.find('count').text))

    print(f'Sum: {sum(digits)}')

# http://py4e-data.dr-chuck.net/comments_42.xml