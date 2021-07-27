from tkinter import Frame, filedialog
from src.log import logger
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master, extract_function, organizer_function):
        logger.info("Starting application...")
        super().__init__(master)
        self.master = master
        self.master.configure(background="orange")
        self.frame = Frame(self.master)
        self.frame.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.extract_function = extract_function
        self.organizer_function = organizer_function
        self.pack()
        self.initial_setup()
        self.center()
        logger.info("Application started succesfully")

    def initial_setup(self):
        self.extract_button = tk.Button(self.frame)
        self.extract_button.config(width=10, height=2)
        self.extract_button["text"] = "Extract"
        self.extract_button["command"] = self.extract
        self.extract_button.pack()

        self.organize_button = tk.Button(self.frame)
        self.organize_button.config(width=10, height=2)
        # self.organize_button.place(anchor=tk.CENTER)
        self.organize_button["text"] = "Organize"
        self.organize_button["command"] = self.organizer
        self.organize_button.pack()
    
    def dispatch(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        frm_width = self.master.winfo_rootx() - self.master.winfo_x()
        win_width = width + 2 * frm_width
        height = self.master.winfo_height()
        titlebar_height = self.master.winfo_rooty() - self.master.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.master.winfo_screenwidth() // 2 - win_width // 2
        y = self.master.winfo_screenheight() // 2 - win_height // 2
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.master.deiconify()

    def exit(self):
        logger.info("Destroying master...")
        self.master.destroy()

    def extract(self):
        self.master.withdraw()
        try:
            logger.info("Calling the extract module")
            self.extract_function()
        except:
            logger.info("Module 'extract' closed unexpectedly")
            pass
        self.master.deiconify()

    def organizer(self):
        self.master.withdraw()
        try:
            logger.info("Calling the organizer module")
            self.organizer_function()
        except:
            logger.info("Module 'organizer' closed unexpectedly")
            pass
        self.master.deiconify()

class Utils:
    def __init__(self):
        self.master = tk.Tk()
        self.master.withdraw()

    def start(self, msg):
        logger.info(msg)
        self.msg = msg
        self.start_info = tk.messagebox.askokcancel(title="Choose folder", message=self.msg)
        if not self.start_info:
            self.master.destroy()
        self.master.destroy()
    
    def get_path(self):
        logger.info("Asking directory")
        self.path = filedialog.askdirectory()
        self.master.destroy()
        if(self.path != ""):
            return self.path
        else:
            exit()

    def are_you_sure(self, msg):
        logger.info(msg)
        self.msg = msg
        self.question = tk.messagebox.askyesno(title="Confirm", message=self.msg)
        logger.info(self.question)
        if self.question:
            self.master.destroy()
        else:
            self.master.destroy()
            exit()

class Message_Error:
    def __init__(self, error_title, error_message):
        self.error_title = error_title
        self.error_message = error_message
        self.master = tk.Tk()
        self.master.withdraw()
        self.msgbox = tk.messagebox.showerror(title=self.error_title, message=self.error_message)
        self.master.destroy()