import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from urllib.request import urlopen

import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = " http://py4e-data.dr-chuck.net/comments_198363.xml"
xmlstring = urlopen(url, context=ctx).read()

stuff = ET.fromstring(xmlstring)
lst = stuff.findall('comments/comment')
print('Comments count:', len(lst))
totalcount = 0

for item in lst:
    totalcount = totalcount + int(item.find('count').text)
print('The total count of comments is:',totalcount)

