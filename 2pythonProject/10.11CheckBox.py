# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
window.geometry('500x500')

check_box_1 = IntVar()
check_box_2 = IntVar()
check_box_3 = IntVar()

chk_btn_1 = Checkbutton(window, text = "apple" , onvalue=1, offvalue=0, height=2, width=10)
chk_btn_2 = Checkbutton(window, text = "mango" , onvalue=1, offvalue=0, height=2, width=10)
chk_btn_3 = Checkbutton(window, text = "plum" , onvalue=1, offvalue=0, height=2, width=10)

chk_btn_1.pack()
chk_btn_2.pack()
chk_btn_3.pack()

# step4: main loop
mainloop()