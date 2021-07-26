import os
from src.tk_utils import Message_Error

def check_structure(path, desired_name):
    folder = path + '/' + desired_name
    if(not os.path.isdir(folder)):
        try:
            os.mkdir(folder)
        except:
            msg = "Could not create folder " + folder
            Message_Error(error_title="Error", error_message=msg)
            exit()