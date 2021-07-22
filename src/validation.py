import os
from src.tk_utils import Message_Error

def check_structure(path):
    extracted = path + '/extracted'
    if(not os.path.isdir(extracted)):
        try:
            os.mkdir(extracted)
        except:
            msg = "Could not create folder " + extracted
            Message_Error(error_title="Error", error_message=msg)
            exit()