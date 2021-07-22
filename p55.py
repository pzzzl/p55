import tkinter as tk
from src.config.config import *
from src.tk_utils import Application
from src.extract_module import extract

if(__name__ == '__main__'):
    root = tk.Tk()
    root.title(APP_NAME)
    root.geometry(APP_GEOMETRY)
    
    app = Application(root, extract)
    app.mainloop()