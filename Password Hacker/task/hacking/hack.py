import socket
import sys


address, port, msg = sys.argv[1], int(sys.argv[2]), sys.argv[3]
my_socket = socket.socket()
my_socket.connect((address, port))
my_socket.send(msg.encode())
response = my_socket.recv(1024)
print(response.decode())
my_socket.close()
