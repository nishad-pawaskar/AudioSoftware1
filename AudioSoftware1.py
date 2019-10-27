import matplotlib
import os, sys
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
audio = filedialog.askdirectory(title = "Select folder with .wav files")        #Open Dialog box to choose path for .wav files
print('Selected directory with audio files: ', audio)
if(audio is ""):
    print("\tFolder with Audio files not selected..!!")

with os.scandir(audio) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('wav'):
            print(entry.name)

root = Tk()
root.withdraw()
mat = filedialog.askdirectory(title = "Select folder with .mat files")          #Open Dialog box to choose path for .mat files
print('Selected directory with data files: ', mat)
if(mat is ""):
    print("\tFolder with Data files not selected..!!")

with os.scandir(mat) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('mat'):
            print(entry.name)