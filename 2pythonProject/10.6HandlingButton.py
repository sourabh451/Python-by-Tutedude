# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
window.title("Simple")
window.geometry('500x500')

def log_entry():
    print("Logged in")

button = Button(window , text = "LOGIN" , command= log_entry , width = 12 , bg = "red" , fg = "white" , font =("bold",12) , activebackground="black" , activeforeground="white")
button.pack()

# step4: main loop
mainloop()