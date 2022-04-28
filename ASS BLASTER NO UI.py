import os
import tkinter
from pygame import mixer
from time import sleep

dir = os.getcwd()
VOX = os.listdir(dir + "./VOX")
TEXT = str(VOX).replace(".wav", "")
ASS_VOLUME = 100

mixer.init()
Channel = mixer.Channel(1)

inputText = input('TIME TO BLAST ASS:\n')

def Blast_ass(v):
    Channel.set_volume(v/100)
    for i in inputText.replace("!", "").replace("\"", "").replace("?", "").replace(",", ".").replace(".", " .").split():
        if i == ".":
            sleep(0.5)
        else:
            try:
                Speak = mixer.Sound("VOX\\"+i+".wav")
                mixer.Channel(1).play(Speak)
                while Channel.get_busy() == True:
                    pass
            except:
                pass

Blast_ass(ASS_VOLUME)