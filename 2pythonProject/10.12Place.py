# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
window.geometry('500x500')

button = Button(window, text = "Button", width=12)
button.place(x=25,y=25)

# step4: main loop
mainloop()