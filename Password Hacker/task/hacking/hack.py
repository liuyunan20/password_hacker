import socket
import sys
import itertools
import string
import os


def hack_password(address, port):
    my_socket = socket.socket()
    my_socket.connect((address, port))
    os.chdir('/Users/liudawei/Desktop/Password Hacker/Password Hacker/task/hacking')
    with open('passwords.txt', 'r') as password_file:
        for line in password_file:
            letters = list(zip(list(line.strip().lower()), list(line.strip().upper())))
            passwords = itertools.product(*letters)
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


result = hack_password(sys.argv[1], int(sys.argv[2]))

print(result)

