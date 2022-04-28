import os
import tkinter
from pygame import mixer
from time import sleep
from tkinter import ttk
from tkinter import *

dir = os.getcwd()
VOX = os.listdir(dir + "./VOX")
TEXT = str(VOX).replace(".wav", "")
ASS_VOLUME = 100

root = Tk()
root.geometry("350x100")
root.title("ASS BLAST USA!")
frm = ttk.Frame(root, padding=15)
frm.grid()


mixer.init()
Channel = mixer.Channel(1)

inputText = tkinter.StringVar()

thelabel = ttk.Label(frm, text="ASS BLAST USA!").grid()
entryBoxs = ttk.Entry(frm, textvariable=inputText)
entryBoxs.insert(END, 'WOOP WOOP ASS BLAST USA! ASS BLAST USA!')
entryBoxs.grid(ipadx=100, ipady=1)

def Blast_ass(v):
    inputText = entryBoxs.get()
    Channel.set_volume(v/100)
    for i in inputText.replace("!", " .").replace("\"", "").replace("?", " .").replace(",", ".").replace(".", " .").split():
        if i == ".":
            sleep(0.5)
        else:
            try:
                Speak = mixer.Sound("VOX\\"+i+".wav")
                mixer.Channel(1).play(Speak)
                print(i)
                while Channel.get_busy() == True:
                    pass
            except:
                print(i+" (WORD NOT IN LIST)")

playButton = ttk.Button(frm, text="Speak", command=lambda : Blast_ass(ASS_VOLUME)).grid()

root.mainloop()  