import xml.etree.ElementTree as ET

data = """<commentinfo>
    <name>Ifeanyi</name>
    <name>mee</name>
    <phone type="intl">
        +234 812 914 1530
    </phone>
    <email hide="yes"/>
</commentinfo>""" 

tree = ET.fromstring(data)
print('Name:', tree.find("name").text)
print('Phone Number:', tree.find("phone").text)
print("Attr:", tree.find('email').get('hide'))