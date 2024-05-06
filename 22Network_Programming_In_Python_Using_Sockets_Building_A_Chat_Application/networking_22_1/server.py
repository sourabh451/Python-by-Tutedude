import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET AF is address family and INET is socket type on ip address and SOCK_STREAM is socket type on TCP

HOST_NAME = socket.gethostname()
#IP = '127.0.0.0' as we are same computer we use host name
#print(HOST_NAME)
PORT = 12345

s.bind((HOST_NAME,PORT))

s.listen(4) # 4 is called backlog specifies accepted connection that the system allows refusing new connection this is consern with multiply client to server this is used to liten connection from client

while True:
    client, address = s.accept()
    client.send(bytes("Hey there, whats up? I am learning to code, I am feeling good","utf-8")) # we can send message through bytes
    print(address)
    client.close()
