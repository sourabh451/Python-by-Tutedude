# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
menu = Menu(window)
file = Menu(menu , tearoff = 0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_separator()
file.add_command(label="Exit" , command= window.quit)

menu.add_cascade(label = "File" , menu = file)
window.config(menu = menu)



# step4: main loop
mainloop()