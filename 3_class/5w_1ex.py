# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_198361.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0 ## Initiate Sum
count = 0 ## initiate Count
for tag in tags:
    # Look at the parts of a tag
    ## print('TAG:', tag)
    ## print('URL:', tag.get('href', None))
    ## print('Contents:', tag.contents[0]) ## Print out all the numbers
    count = count + 1
    sum = sum + int(tag.contents[0]) ## sum up all the numbers
    ## print('Attrs:', tag.attrs)
print('Count:',count,'\nSum:',sum) ## print all the numbers at the end