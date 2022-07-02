# Using Web Services
# https://www.py4e.com/lessons/servces
from urllib import request
import xml.etree.ElementTree as ET

a=request.urlopen("http://py4e-data.dr-chuck.net/comments_1550331.xml")
b=a.read()
c=ET.fromstring(b)
d=c.findall("comments/comment")
sum=0
for i in d:
    sum+=int(i.find("count").text)
print(sum)