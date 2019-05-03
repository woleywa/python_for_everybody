import xml.etree.ElementTree as ET

# input = '''
# <stuff>
#   <users>
#     <user x="2">
#       <id>001</id>
#       <name>Chuck</name>
#     </user>
#     <user x="7">
#       <id>009</id>
#       <name>Brent</name>
#     </user>
#   </users>
# </stuff>'''

input = "http://py4e-data.dr-chuck.net/comments_42.xml"

stuff = ET.fromstring(input)
lst = stuff.findall('comments/comment')
print('Comments count:', len(lst))

# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get('x'))
