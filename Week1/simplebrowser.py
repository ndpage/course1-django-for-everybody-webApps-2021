import socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(('data.py4e.org',80))
cmd = 'GET http://data.py4e.org/page1.html HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
  data = mysocket.recv(512)
  if len(data)<1:
    break
  print(data.decode(), end='')

mysocket.close()