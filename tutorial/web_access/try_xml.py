import xml.etree.ElementTree as ET
 

data = """
<person>
    <name>Ifeanyi</name>
    <phone type="intl">
     +234 812 974 1530
    </phone>
    <email hide="yes"/>
</person>"""

tree = ET.fromstring(data)
print("Name:", tree.find('name').text)
print("Email:", tree.find('email').get('hide'))