import socket
import sys

target = sys.argv[1]
request_text = f"GET / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n"
request_bytes = request_text.encode('ISO-8859-1')

s = socket.socket()
s.connect((target, 80))
s.sendall(request_bytes)

""" Get response in chunks of 1024 bytes, d is the buffer and it all gets sent
    eventually to answer.
"""
d = s.recv(1024)
answer = d
while len(d) != 0:
    d = s.recv(1024)
    answer = answer.__add__(d)

""" Wrap it up and print out the answer gotten from the server.
"""
s.close()
answer = answer.decode('ISO-8859-1')
print(answer)