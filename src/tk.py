from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os

def get_path():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    root.destroy()
    if(path != ""):
        return path
    else:
        exit()

def start():
    root = tk.Tk()
    root.withdraw()
    start_info = tk.messagebox.askokcancel(title="Choose folder", message='Choose the directory tree which will have all files extracted to a single folder "extracted".')
    if not start_info:
        exit()
    root.destroy()

def are_you_sure(path):
    root = tk.Tk()
    root.withdraw()
    question = tk.messagebox.askyesno(title="Confirm", message='Are you sure you want to extract all files from the folder "' + path + '" into a single folder "extracted"?')
    if question:
        root.destroy()
    else:
        root.destroy()
        exit()