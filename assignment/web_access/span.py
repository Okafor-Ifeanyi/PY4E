from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
total = None
count = 0
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None)) 
    if total == None:
        total = tag.contents[0]
    else:
        total = int(total)
        total += int(tag.contents[0])
    count += 1
    # print(tag.contents[0])
    # print('Attrs:', tag.attrs)

print(f"Count = {count}")
print(f"Total score = {total}")