from tkinter import *
from tkinter import messagebox
# import numpy as np
import time

# APARIENCIA DE LA GUI

# root = Tk()                                                                 # Mengisi variabel root dengan TK() dari tkinter                
# root.geometry("500x500")                                                    # Mengatur ukuran window GUI sebesar 500x500
# root.iconbitmap("D:\Coding\Python\Tkinter Project\Matrix Calculator\matrix.ico")   # Memberi icon pada GUI yang diambil dari folder
# root.title("City Traffic Mannager / 19081010001")                        # Mengatur title GUI yang terletak dikanan icon
# root.configure(bg = "#474E64")  




window = Tk()

window.title("City Traffic Manager")
window.geometry("500x500")
window.configure(bg = "#474E64")

lbl = Label(window, text = "\nWelcome back!\nCity Traffic Manager is ready to use.\n", font=("Consolas", 10), width = 100, height = 4)
lbl.grid (column = [1], row = 0)

def clicked():
   window = Tk()
   window.title("Traffic Data")
btnmec = Button(window, text="Start", font=("Consolas", 12), bg="midnightblue", fg="mintcream", width = 8, command=clicked)
btnmec.grid(column=0, row=1)


window.mainloop()

