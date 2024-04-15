# step1: import tkinter
from tkinter import *
import tkinter.messagebox

# step2: gui interaction
window = Tk()

# step3: adding inputs
# tkinter.messagebox.showinfo("Info" , "Running out time")
# tkinter.messagebox.showwarning("Info" , "Running out time")
# tkinter.messagebox.showerror("Info" , "Running out time")
question = tkinter.messagebox.askyesno("Weather" , "Will it rain")

if question == True:
    print("Take an umbrella")
else:
    print("Okay")

# step4: main loop
mainloop()