import socket
import sys

port = sys.argv[1]

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', int(port)))
s.listen()

while True:
    new_conn = s.accept()
    new_socket = new_conn[0]

    """ Get request in chunks of 1024 bytes, r is the buffer and it all gets sent
        eventually to request.
    """
    r = new_socket.recv(1024)
    request = r
    while len(r) != 0:
        r = new_socket.recv(1024)
        request = request.__add__(r)

    request = request.decode('ISO-8859-1')
    print(request)
