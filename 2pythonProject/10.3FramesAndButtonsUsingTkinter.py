# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
window.title("Simple")
window.geometry("500x700")
window.config(bg = "yellow")
#frame1 = Frame(window , bg = "red", width = 300 , height = 300 , cursor = "dot")
#frame2 = Frame(window , bg = "green", width = 300 , height = 300, cursor = "dotbox")
frame1 = Frame(window , width = 300 , height = 300 , cursor = "dot")
frame2 = Frame(window , width = 300 , height = 300, cursor = "dotbox")

button1 = Button(frame1 , text = "Button1" , bg = "blue" )
button2 = Button(frame2 , text = "Button2" , bg = "green" )
button3 = Button(frame1 , text = "Logged" , fg = "red" )

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
button3.pack()

# step4: main loop
mainloop()
