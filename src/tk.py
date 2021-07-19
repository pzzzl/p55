from tkinter import filedialog
import tkinter as tk
import os

def get_path():
    window = tk.Tk()
    window.withdraw()
    path = filedialog.askdirectory()
    window.destroy()
    if(path != ""):
        return path
    else:
        exit()