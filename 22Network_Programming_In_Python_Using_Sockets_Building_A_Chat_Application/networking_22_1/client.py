import socket
from tkinter import *

def send(listbox,entry):
    message = entry.get()
    listbox.insert('end', "Client: "+message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    recieve(listbox)

def recieve(listbox):
    message = s.recv(50)
    listbox.insert('end', "Server: "+message.decode('utf-8'))

root = Tk()

entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root,text="Send",command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root,text="Recieve",command=lambda :recieve(listbox))
rbutton.pack(side=BOTTOM)
root.title('Client')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME,PORT))
# Run server and then client and check server terminal it will give one ip address for both server and client because we r using the same computer

#msg = s.recv(100) # 100 is buffer size
#print(msg.decode('utf-8'))

'''
msg = s.recv(10)
msg1 = s.recv(10)
print(msg.decode('utf-8'))
print(msg1.decode('utf-8'))
'''

'''
while True:
    message = ''
    while True:
        msg = s.recv(10)
        if len(msg)<=0:
            break
        message += msg.decode("utf-8")
    if len(message)>0:
        print(message)
'''

'''
while True:
    #message = s.recv(50)
    print("Server:"+message.decode('utf-8'))

    message_to_send = input('Client:')
    #s.send(bytes(message_to_send,"utf-8"))
'''

root.mainloop()
