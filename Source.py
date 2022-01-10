from tkinter import *
window = Tk()

window.title("ROBOLEARN")

lbl = Label(window, text = "\nArea:", font=("Century Gothic", 20))
lbl.grid (column = 0, row = 0)

btnmec = Button(window, text="Mechatronics", font=("Century Gothic", 12), bg="midnightblue", fg="mintcream", width = 14)
btnmec.grid(column=0, row=1)
btnprgm = Button(window, text="Programming", font=("Century Gothic", 12), bg="forestgreen", fg="azure", width = 14)
btnprgm.grid(column=0, row=2)
btnb = Button(window, text="Bussiness", font=("Century Gothic", 12), bg="midnightblue", fg="mintcream", width = 14)
btnb.grid(column=0, row=3)
btni = Button(window, text = "Merchandising", font=("Century Gothic", 12), bg="forestgreen", fg="azure", width = 14)
btni.grid(column = 0, row = 4)
btnwb = Button(window, text = "Well being", font=("Century Gothic", 12), bg="midnightblue", fg="mintcream", width = 14)
btnwb.grid(column = 0, row = 5)
btnl = Button(window, text = "Leadership", font=("Century Gothic", 12), bg="forestgreen", fg="azure", width = 14)
btnl.grid(column = 0, row = 6)
window.mainloop()