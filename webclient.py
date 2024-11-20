import socket

target = 'google.com'

s = socket.socket()
s.connect((target, 80))
s.sendall(b'GET / HTTP/1.1\r\nHost: google.com\r\nConnection: close\r\n\r\n')
d = s.recv(1024)

#while len(d) != 0:
#    d = s.recv(1024)

s.close()
answer = d.decode('ISO-8859-1')
print(answer)