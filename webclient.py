import socket

s = socket.socket()
s.connect(('google.com', 80))
s.sendall(b'GET / HTTP/1.1\r\nHost: google.com\r\nConnection: close\r\n\r\n')
d = s.recv(1024)

#while len(d) != 0:
#    d = s.recv(1024)

s.close()
print(d)