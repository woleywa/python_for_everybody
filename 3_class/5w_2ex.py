import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = " http://py4e-data.dr-chuck.net/known_by_Karn.html"
# maxcount = int(input("Please insert the depth of your search: "))
# position = int(input("Please enter the position: ")) - 1
maxcount = 7
position = 17
# count = 0
print(re.findall('known_by_(.+)\.html',url)[0])
for i in range(maxcount):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	links = soup('a')
	url = links[position].get('href', None)
	print(re.findall('known_by_(.+)\.html',url)[0])

