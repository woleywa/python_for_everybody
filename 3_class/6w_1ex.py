import urllib.request, urllib.parse, urllib.error
import json
import ssl
from urllib.request import urlopen

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = " http://py4e-data.dr-chuck.net/comments_198364.json"
xmlstring = urlopen(url, context=ctx).read()

# data = '''[ "Glenn", "Sally", "Jen" ]'''
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
total_count = 0
for users in info['comments']:
  total_count += users['count']
print("The total count is:",total_count)