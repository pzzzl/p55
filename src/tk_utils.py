from tkinter import filedialog
import tkinter as tk
# from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master, extract_function):
        super().__init__(master)
        self.master = master
        self.extract_function = extract_function
        self.pack()
        self.initial_setup()

    def initial_setup(self):
        self.extract_button = tk.Button(self)
        self.extract_button["text"] = "Extract"
        self.extract_button["command"] = self.extract
        self.extract_button.pack()

        self.organize_button = tk.Button(self)
        self.organize_button.place(anchor=tk.CENTER)
        self.organize_button["text"] = "Organize"
        self.organize_button["state"] = "disabled"
        self.organize_button.pack()
    
    def dispatch(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def exit(self):
        self.master.destroy()

    def extract(self):
        self.extract_function()
        self.exit()

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