#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
#source:http://data.pr4e.org/intro-short.txt
#doing this dated 110622
# Object Oriented Programming
# https://www.py4e.com/lessons/Objects



import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
  data = mysock.recv(512)
  if len(data) < 1:
    break
  print(data.decode(),end='')

mysock.close()

