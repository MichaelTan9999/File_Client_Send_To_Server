import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("ServerIP: "+socket.gethostbyname(socket.gethostname()))


ServerIP = socket.getfqdn(socket.gethostname())

ServerPort = 12000
print("ServerPort: "+str(ServerPort)+".")

Max_Of_Connection = 1

print("The maximum of the connections: ", Max_Of_Connection)

s.bind((ServerIP, ServerPort))

s.listen(Max_Of_Connection)

print("Waiting for connections...")

(ClientIP, ClientPort) = s.accept()

print('ClientIP: ', ClientIP)
print('ClientPort', ClientPort)

while True:
    with open("file","ab") as f:
        data = ClientIP.recv(1024)
        if data == b'quit':
            #print('The client asks to end the service.')
            break
        f.write(data)
    ClientIP.send("success".encode())
print("Successfully received the target file.")
s.close()
