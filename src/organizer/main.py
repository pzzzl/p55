from src.tk_utils import Utils
import src.validation as validation
import src.organizer.routine as routine

def organizer():
    Utils().start(msg="Choose the directory which will have it's files organized by extension.")
    path = Utils().get_path()
    Utils().are_you_sure(msg='Are you sure you want to organize all files from the root folder "' + path + '" by extension?')
    validation.check_structure(path, "organized")
    routine.run(path)