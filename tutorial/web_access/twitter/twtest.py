from ast import arguments
from multiprocessing import connection
import urllib.request, urllib.parse, urllib.error
from twurl import argument
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

print('* Calling Twitter...')
url = argument("https://api.twitter.com/1.1/statues/user_timeline.json",
                {'screen_name': '', 'count': '2'})
print(url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

headers = dict()
print(headers)
