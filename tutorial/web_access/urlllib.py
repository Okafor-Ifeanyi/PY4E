import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

url = input("Enter Url: ")
fhand = urllib.request.urlopen(url).read()
soup = BeautifulSoup(fhand, "html.parser")

data = (f'"""{soup}"""')
print(data)
stuff = ET.fromstring(data)
# user = stuff.findall('comments/comment')
# print('User count:', len(user))
# digits = []
# for item in user: 
#     print('Name: ', item.find('name').text)
#     print('Number:',item.find('count').text)
#     digits.append(int(item.find('count').text))
    # print('id: ', i.find('id').text)
    # print('Attribute', i.get("x"))

# print(sum(digits))


# tag = soup('a')
# for links in tag:
#     print(links.get('href', None))




# for line in fhand:
#     words = line.decode().split()
#     print(words)


    
