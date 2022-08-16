import json
import urllib.request, urllib.error, urllib.parse
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
    html = urllib.request.urlopen(url)
    input = html.read()
    print('Retrieved', len(input), 'characters')

    data = json.loads(input)
    print("User count ", len(data['comments']))
    
    digits = []
    for item in data['comments']:
        # print("Num", item['count'])
        # print('Name', item['name'])
        digits.append(int(item['count']))


    print(sum(digits))

# http://py4e-data.dr-chuck.net/comments_42.json