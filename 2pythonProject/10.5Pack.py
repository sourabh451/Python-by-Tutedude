# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
window.title("Simple")
window.geometry('500x500')

label1 = Label(window , text = "Label-1", bg = "red" , fg = "white")
label2 = Label(window , text = "Label-2", bg = "blue" , fg = "white")
label3 = Label(window , text = "Label-3", bg = "green" , fg = "white")

label1.pack(side = TOP , fill = X , expand = False)
label2.pack(side = LEFT , fill = Y , expand = False)
label3.pack(side = RIGHT , fill = Y , expand = False)

# step4: main loop
mainloop()