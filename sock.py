import socket

print 'Socket lib utility functions'
print 'This machine\'s hostname: %s' % socket.gethostname()
print 'Does this OS support IPv6? %s' % socket.has_ipv6
print 'Get addr info of google.com:80 %s' % socket.getaddrinfo('google.com', 80)
print 'IP address of loopback/localhost? %s' % socket.gethostbyname('localhost')

print ''

s = socket.socket()
print 'Default address family of my new socket: %s' % s.family
print 'Default type of my new socket: %s' % s.type
print s.getsockname()
