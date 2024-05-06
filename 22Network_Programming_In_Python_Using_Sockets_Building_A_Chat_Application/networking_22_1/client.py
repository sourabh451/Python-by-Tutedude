import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME,PORT))
# Run server and then client and check server terminal it will give one ip address for both server and client because we r using the same computer
msg = s.recv(100) # 100 is buffer size 
print(msg.decode('utf-8'))