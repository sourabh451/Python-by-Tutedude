# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
window.geometry('500x500')
'''
message = Message(window, text = "Python")
message.pack()
'''

'''
var = StringVar()
message = Message(window, textvariable=var , relief=RAISED , padx = 20, pady = 20)
var.set("Welcome")
message.pack()
'''

var = StringVar()
ent_var = StringVar()

def insert():
    result = ent_var.get()
    var.set(result)

message = Message(window , textvariable=var, relief=RAISED, padx = 50, pady= 50)
entry = Entry(window, textvariable= ent_var)
button = Button(window, text="OK", command = insert)
message.pack()
entry.pack()
button.pack()

# step4: main loop
mainloop()