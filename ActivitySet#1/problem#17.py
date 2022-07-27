import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


def main():
  url = 'http://py4e-data.dr-chuck.net/known_by_Leno.html'
  for i in range(7):
    tags = find(url)
    l=list()
    for tag in tags:
      k=tag.get('href', None)
      l.append(k)
    url=l[17]
  print(url)
  

def find(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    return tags


main()