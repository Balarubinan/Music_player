# temporary store for code
# old version play_music
# old version of rewind music removed due to error of counter while rewinding
def rewind_music():
    global flg
    if (flg==1):
        statbar['text'] = "No Loaded Music"
    else:
        mixer.music.play()
        statbar['text'] = "Re-winded to beginning"
        flg = 0

def del_playlist():
    global file
    #index=playlistbox.index(os.path.basename(file.name))
    sel_song = playlistbox.curselection()
    sel_song = int(sel_song[0])
    # print(playlist)
    playlist.remove(playlist[sel_song])
    for x in playlistbox:
        print(x,end=" ")
    playlistbox.delete(os.path.basename(playlist[sel_song]))
# discontinued due to complexity of function
def play_music():
    global flg
    global filename
    global loaded
    try:
        if (flg == 0):
            if (loaded is False):
                sel_song=playlistbox.curselection()
                sel_song=int(sel_song[0])
                filename=playlist[sel_song].name
                # sel_song=str(playlistbox[sel_song].name)
                #print(sel_song,"1")playlist[sel_song].name
                # work on this function
                mixer.music.load(""+playlist[sel_song].name)
                mixer.music.play()
                statbar['text'] = "Playing" + ' ' + os.path.basename(filename)
                loaded = True
            else:
                mixer.music.unpause()
                statbar['text'] = "Resumed" + ' ' + os.path.basename(filename)
            # the os.path.basename returns the file name without the path of the file
            flg = 1
        else:
            if (loaded):
                mixer.music.pause()
            else:
                mixer.music.stop()
            flg = 0
            statbar['text'] = "Music is Paused"
        # show_details()
    except:
        # This Handles all the format exceptions too no need to check explicitly for mp3
        print(sys.exc_info())
        tkinter.messagebox.showerror("Error Playing File!",
                                     "Music Player Could'nt find the specified file check it again")


