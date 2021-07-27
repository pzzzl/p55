import tkinter as tk
from config.config import *
from src.tk_utils import Application
from src.extract.main import extract
from src.organizer.main import organizer

if(__name__ == '__main__'):
    root = tk.Tk()
    root.title(APP_NAME)
    root.geometry(APP_GEOMETRY)
    
    app = Application(root, extract, organizer)
    app.mainloop()