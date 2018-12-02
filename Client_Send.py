import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerIP = input("Enter the IP address of the server: ")
ServerPort = int(input("Enter the port of the server: "))

s.connect((ServerIP, ServerPort))

filepath = '/Users/michaeltansbook/Desktop/123.txt'

with open(filepath, "rb") as f:
    for i in f:
        s.send(i)
        data = s.recv(1024)
        if data != b'success':
            break
s.send('quit'.encode())
s.close()
