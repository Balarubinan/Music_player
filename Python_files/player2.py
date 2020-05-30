from tkinter import *
import tkinter as tk
from pygame import mixer
import tkinter.messagebox

from tkinter import ttk
from tkinter import filedialog
import os

root = Tk()
root.resizable(False, False)

play = PhotoImage(file="play.PNG")
pause = PhotoImage(file="pause.png")
next = PhotoImage(file="next.png")
back = PhotoImage(file="back.png")
stop = PhotoImage(file="stop.png")

def change():
    pausebtn['image']=back
    pausebtn.grid()

stopbtn = Button(root, image=stop)
stopbtn.grid(row=0,column=0)

playbtn = Button(root, image=play)
# btn=Button(root,text="click")
playbtn.grid(row=1,column=1)

pausebtn = Button(root, image=pause,command=change)
pausebtn.grid(row=2,column=2)

root.mainloop()