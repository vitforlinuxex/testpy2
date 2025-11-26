from gtts import gTTS
from io import BytesIO
import pygame
import time
import os
import sys



#      VERSION CLI

def wait():
    # print(pygame.mixer.get_busy())
    while pygame.mixer.get_busy():
        time.sleep(.1)

def speak(text="", language='it', tld='it'):
    ''' speaks without saving the audio file '''
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    sound.play()
    wait()


pygame.init()
pygame.mixer.init()
parla = input("Parla: ")
speak(parla)