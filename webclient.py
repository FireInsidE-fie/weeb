import socket

target = 'renshuu.org'

s = socket.socket()
s.connect((target, 80))
s.sendall(b'GET / HTTP/1.1\r\nHost: google.com\r\nConnection: close\r\n\r\n')
d = s.recv(1024)
answer = d
while len(d) != 0:
    d = s.recv(1024)
    answer = answer.__add__(d)

s.close()
answer = answer.decode('ISO-8859-1')
print(answer)