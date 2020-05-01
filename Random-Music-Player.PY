
# Author: @Ameta_Programmer:
import os
import random
from tkinter import *

x = random.randint(1 , 46)
# y = 'play'
def play_song():
    music_dir = 'F:\\music'  # Enter your music directory path
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[x]))


if __name__ == '__main__':

    root = Tk()
    root.title("Random music player")
    root.geometry("325x225")

    f = Frame(root)
    f.pack()

    b1 = Button(f, text = "Play", pady = 20, padx = 20, command = play_song )
    b1.pack()

    root.mainloop()

















