# Project Status:Completed (YAAAAAAAAYYYYY!!)
# stated on:1/1/2020 finished on: 15/1/2020 Duration:15 days
# project name: Music Player
# Learnt things :Basic python GUI,Threading Concept
# DeBugging : Done As Much As Possible
# Difficulty : Beginner (duh!! this is my first project)

import cx_Freeze
from pygame import mixer
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
import os
import threading
import math
from mutagen.mp3 import MP3
import time
from ttkthemes import themed_tk as tk

# Pack always arranges the widgets down to down
flg = 0
# controls the play button presses
muted = False
# used to check the last value for the mute button
file = None
loaded = False
filename = ""


# Function Declarations
def show_details():
    formt = os.path.basename(filename).split(".")[1]
    if (formt == "mp3"):
        audio = MP3(filename)
        ttllen = audio.info.length
    else:
        a = mixer.Sound(filename)
        ttllen = a.get_length()
    m, s = divmod(ttllen, 60)
    m = round(m)
    s = round(s)
    tte = '{:02d}:{:02d}'.format(m, s)
    lenlabel['text'] = "Total Length " + tte
    # start_count(ttllen)
    t1 = threading.Thread(target=start_count, args=(ttllen,))
    t1.start()


# work on this function    global flg
#     if(flg==0):
# bug exists check later
def start_count(t):
    while t > 0 and mixer.music.get_busy():
        if (flg == 1 or loaded is False):
            continue
        else:
            m, s = divmod(t, 60)
            m = round(m)
            s = round(s)
            tte = '{:02d}:{:02d}'.format(m, s)
            curtym['text'] = "Current Length " + tte
            time.sleep(1)
            t -= 1
    # print(mixer.music.get_busy(),"at ",tte)


# flg=1 paused mode flg=0 playing mode
def play_music():
    global flg, filename, loaded
    if (flg == 1):
        mixer.music.unpause()
        flg = 0
        statbar['text'] = "Resumed" + ' ' + os.path.basename(filename)
    else:
        try:
            stop_music()
            time.sleep(1)
            sel_song = playlistbox.curselection()
            # returns a tuple with curent selection index
            sel_song = int(sel_song[0])
            filename = playlist[sel_song].name
            # sel_song=str(playlistbox[sel_song].name)
            # print(sel_song,"1")playlist[sel_song].name
            # work on this function
            mixer.music.load("" + playlist[sel_song].name)
            mixer.music.play()
            statbar['text'] = "Playing" + ' ' + os.path.basename(filename)
            flg = 0
            loaded = True
            show_details()
        except:
            # This Handles all the format exceptions too no need to check explicitly for mp3
            print(sys.exc_info())
            tkinter.messagebox.showerror("Error Playing File!",
                                         "Music Player Could'nt find the specified file check it again")


def stop_music():
    global loaded
    global flg
    mixer.music.stop()
    loaded = False
    statbar['text'] = "Stopped Playing"
    flg = 0


def pause_music():
    global flg
    if (flg == 1):
        statbar['text'] = "No Music is playing to be paused"
    else:
        mixer.music.pause()
        statbar['text'] = "Music is paused"
        flg = 1


def rewind_music():
    if (flg == 1):
        statbar['text'] = "No Loaded Music"
    else:
        stop_music()
        play_music()


def set_vol(val):
    # here the value from the Scale widget is automatically sent to this function via the "val" variable
    vol = float(val) / 100
    global muted
    if (muted is not True):
        mixer.music.set_volume(vol)
    # accept value only in range [0,1]


def abt_me():
    tkinter.messagebox.showinfo("Music Player 3.3.1",
                                "This is a Simple Music player made for practice and getting a grip on python's Tkinter module as a Beginner.")


def mute_music():
    global muted
    if (muted == True):
        soundbtn.configure(image=sound)
        mixer.music.set_volume(scale.get() / 100)
        muted = False
    else:
        soundbtn.configure(image=mute)
        muted = True
        mixer.music.set_volume(0)


# the configure method is a much cleaner method than the soundbtn['image'] method
# it allows us to modify a image button without the pack thingy
def browse():
    global file, flg
    file = filedialog.askopenfile()
    # file.name = "music.mp3"
    # if (file == None):
    #     tkinter.messagebox.showerror("No File selected", "Please select a file to play")
    # else:
    #    play_music()
    if (file.name.endswith(".mp3") or file.name.endswith(".wav")):
        create_playlist(file)
    else:
        tkinter.messagebox.showerror("Unsupported Format!!", "Please select audio files only")


# list for saving added files as the playlist bod only has the base file name
playlist = []


def create_playlist(file):
    index = 0
    playlistbox.insert(index, os.path.basename(file.name))
    playlist.insert(index, file)
    index += 1


def del_song():
    global filename
    sel_song = playlistbox.curselection()
    # returns a tuple with cureent selection index
    sel_song = int(sel_song[0])
    playlistbox.delete(sel_song)
    # removing the selection from the widget
    playlist.remove(playlist[sel_song])
    # removing selection from the playlist
    # print(playlist)


# i am an idiot , 5 theme funcs for 5 themes :-/
def change_theme1():
    root.set_theme("vista")


def change_theme2():
    root.set_theme("plastik")


def change_theme3():
    root.set_theme("arc")


def change_theme4():
    root.set_theme("blue")


def change_theme0():
    root.set_theme("radiance")


root = tk.ThemedTk()
root.geometry('800x300')
root.resizable(False, False)
root.get_themes()
root.set_theme("radiance")  # plastik radiance arc blue black clam classic deault winnative xpnative vista
statbar = ttk.Label(root, text="Welcome to Music player", relief=SUNKEN, anchor=W, font="times 15 italic")
# relief variable set the elevation of the bar sunken means depressed
# status bar is basically a label stuck to the bottom with some special formatting
# anchor tag sticks the text to the given side W=west and so on
# main window is divided into right_frame and left_frame
# right frame is a composition of top,bot and middle frames
statbar.pack(side=BOTTOM, fill=X)
lframe = Frame(root, padx=30)
lframe.pack(side=LEFT)
rframe = Frame(root, padx=30)
rframe.pack()
topframe = Frame(rframe)
topframe.pack()
# Sets the X and Y of the window as Fixed( ie Non Resizeable)
lenlabel = ttk.Label(topframe, text="Total length : --:-- ")
lenlabel.pack(pady=10)
curtym = ttk.Label(topframe, text="Current length : --:--", relief=GROOVE)
curtym.pack()
mid_frame = ttk.Frame(rframe)
# frame is a division in the main window to organize widgets into groups
# relief and border width attribs can be used to make a frame visible to the user for visual clarity
mid_frame.pack(pady=20, padx=30)
mixer.init()
# ttk.Style().configure('green/black.TLabel',foreground='green',background='black')

# Creating empty menu bar
menubar = Menu(root)
root.config(menu=menubar)
# submenu
submenu = Menu(menubar, tearoff=0)
submenu2 = Menu(menubar, tearoff=0)
submenu3 = Menu(menubar, tearoff=0)
# tear off tag takes out unwanted ------- which appears on default
theme = StringVar(root)
theme.set("vista")
# root2=tk.ThemedTk()
# thememenu=OptionMenu(root2,theme,"vista","plastik","blue","black","clam")
# thememenu.pack()
filepic = PhotoImage(file="images/File.PNG")
menubar.add_cascade(label="File", menu=submenu)
menubar.add_cascade(label="View", menu=submenu2)
menubar.add_cascade(label="Theme", menu=submenu3)
submenu3.add_command(label="Default", command=change_theme0)
submenu3.add_command(label="Vista", command=change_theme1)
submenu3.add_command(label="Plastic", command=change_theme2)
submenu3.add_command(label="Arc", command=change_theme3)
submenu3.add_command(label="Blue", command=change_theme4)
submenu2.add_command(label="About me", command=abt_me)
submenu.add_command(label="Open", command=browse)
submenu.add_command(label="Exit", command=root.destroy)

# basic geometry and initialising stuff
# root.geometry('300x300')
root.title("MusicPlayer")
root.iconbitmap("Demo.ico")

# photo files are basically a wrapper for image files inside python
play = PhotoImage(file="images/play.PNG")
pause = PhotoImage(file="images/pause.png")
next = PhotoImage(file="images/next.png")
rewind = PhotoImage(file="images/back.png")
stop = PhotoImage(file="images/stop.png")
sound = PhotoImage(file="images/sound.png")
mute = PhotoImage(file="images/mute.png")
# LabelPhoto=Label(root,image=photo)
# LabelPhoto.pack()
# nextbtn = Button(root, image=next)
# nextbtn.pack(padx=40, pady=0, side=tk.RIGHT)

# backbtn = Button(root, image=back)
# backbtn.pack(padx=40, pady=0, side=tk.LEFT)

stopbtn = ttk.Button(mid_frame, image=stop, command=stop_music)
stopbtn.grid(row=0, column=0, padx=30)

playbtn = ttk.Button(mid_frame, image=play, command=play_music)
# btn=Button(root,text="click")
playbtn.grid(row=0, column=1, padx=20)

pausebtn = ttk.Button(mid_frame, image=pause, command=pause_music)
pausebtn.grid(row=0, column=2, padx=25)

# new frame to handle the rewind and the scale widgets as one
bot_frame = ttk.Frame(rframe)
bot_frame.pack(pady=10)

rwdbtn = ttk.Button(bot_frame, image=rewind, command=rewind_music)
rwdbtn.grid(row=0, column=0, padx=10)

soundbtn = ttk.Button(bot_frame, image=sound, command=mute_music)
soundbtn.grid(row=0, column=3, padx=10)

Vol_Tag = ttk.Label(root, text="Volume")
Vol_Tag.pack()

# A list box is item view where you can see and select stuff , used here for creating a playlist
playlistbox = Listbox(lframe)
playlistbox.pack()

add_btn = ttk.Button(lframe, text="Add", command=browse)
add_btn.pack(side=LEFT)

del_btn = ttk.Button(lframe, text="Delete", command=del_song)
del_btn.pack(side=LEFT)

scale = ttk.Scale(bot_frame, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)
set_vol(50)
scale.grid(row=0, column=1, padx=29)


# Main Loop

def on_close():
    # start_count thread is running in background so you need to stop it before exiting
    # or else an undesired error is thrown in the console
    # tkinter.messagebox.showinfo('Exit',"Do you really want to exit Music Player?")
    stop_music()
    root.destroy()


# protocol method is used to control the button stuff of default actions
# here "WM_DELETE_WINDOW" denotes the "X" button
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
