# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
inp = Label(window , text = "Hello world!")
inp.pack()

# step4: main loop
window.mainloop()