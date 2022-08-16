from tkinter import E
import xml.etree.ElementTree as ET

input = """<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Ifeanyi</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Okafor</name>
        </user>
    </users>
</stuff>"""

stuff = ET.fromstring(input)
user = stuff.findall('users/user')
print('User count:', len(user))

for i in user:
    print('Name: ', i.find('name').text)
    print('id: ', i.find('id').text)
    print('Attribute', i.get("x"))
    print("\n")