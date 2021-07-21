import tkinter as tk
from src.extract_module import extract
from src.tk_utils import Application

APPLICATION_NAME = "P55"

if(__name__ == '__main__'):
    root = tk.Tk()
    root.geometry("270x50")
    root.title(APPLICATION_NAME)
    app = Application(root, extract)
    app.mainloop()