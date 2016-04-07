import socket

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP type
s.bind((HOST, PORT))
s.listen(1)  # listen with backlog of 1 connection

while 1:
  conn, addr = s.accept()
  print 'Connected by:'
  print addr
  data = conn.recv(2**10)
  # if not data:
  #   break
  conn.sendall('Hi there %s' % data)

conn.close()
