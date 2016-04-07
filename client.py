import socket

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Created client socket: %s' % s

s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(2**10)
s.close()
print 'Received:'
print data
