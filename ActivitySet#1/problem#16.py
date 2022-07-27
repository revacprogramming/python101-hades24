
#doing this dated 110622
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
html = urlopen('http://py4e-data.dr-chuck.net/comments_1543850.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the Span tags
tags = soup('span')
l=list()
sum=0
for span in tags:
    l.append(span.contents[0])
for num in l:
    sum=sum+int(num)
print(sum)