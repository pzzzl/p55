import os
import tkinter as tk
from tkinter import messagebox

class Message_Error:
    def __init__(self, error_title, error_message):
        self.error_title = error_title
        self.error_message = error_message
        self.root = tk.Tk()
        self.root.withdraw()
        self.msgbox = tk.messagebox.showerror(title=self.error_title, message=self.error_message)
        self.root.destroy()

def check_structure(path):
    extracted = path + '/extracted'

    if(not os.path.isdir(extracted)):
        try:
            os.mkdir(extracted)
        except:
            msg = "Could not create folder " + extracted
            Message_Error("Error", msg)
            exit()