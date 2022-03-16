import socket
import sys
import itertools
import string


def hack_password(address, port):
    my_socket = socket.socket()
    my_socket.connect((address, port))
    password_element = list(string.digits + string.ascii_lowercase)
    password_length = 1
    while True:
        passwords = itertools.combinations(password_element, password_length)
        for password in passwords:
            msg = "".join(password)
            my_socket.send(msg.encode())
            response = my_socket.recv(1024)
            if response.decode() == "Connection success!":
                my_socket.close()
                return msg
            if response.decode() == "Too many attempts":
                my_socket.close()
                return "Too many attempts"
        password_length += 1


result = hack_password(sys.argv[1], int(sys.argv[2]))

print(result)

