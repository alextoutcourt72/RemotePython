import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_pc = ""
port = 12345

s.bind((local_pc, port))
s.listen()

while True:
    print("Servers: ")
    conn, addr = s.accept()
    print("[ OK ] Connected " ,addr)

    try:
        while True:
            command = input("Command: ")
            conn.sendall(command.encode())
    except:
        print("[ DISCONNECT ] Disconnected from ", addr)