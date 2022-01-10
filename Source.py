from tkinter import *

window = Tk()

window.title("ROBOLEARN")

lbl = Label(window, text = "\nWelcome\nback!\n", font=("Century Gothic", 12), width = 8, height = 4)
lbl.grid (column = 0, row = 0)

def clicked():
    window = Tk()
    window.title("MEC")
btnmec = Button(window, text="MEC", font=("Century Gothic", 12), bg="midnightblue", fg="mintcream", width = 8, command=clicked)
btnmec.grid(column=0, row=1)
btnprgm = Button(window, text="PRGM", font=("Century Gothic", 12), bg="forestgreen", fg="azure", width = 8)
btnprgm.grid(column=0, row=2)
btnb = Button(window, text="BSS", font=("Century Gothic", 12), bg="midnightblue", fg="mintcream", width = 8)
btnb.grid(column=0, row=3)
btni = Button(window, text = "MERC", font=("Century Gothic", 12), bg="forestgreen", fg="azure", width = 8)
btni.grid(column = 0, row = 4)
btnwb = Button(window, text = "WB", font=("Century Gothic", 12), bg="midnightblue", fg="mintcream", width = 8)
btnwb.grid(column = 0, row = 5)
btnl = Button(window, text = "LS", font=("Century Gothic", 12), bg="forestgreen", fg="azure", width = 8)
btnl.grid(column = 0, row = 6)
window.mainloop()