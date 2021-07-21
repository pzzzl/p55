import src.tk_utils as tk_utils
import src.validation as validation
import src.routine as routine

def extract():
    tk_utils.start()
    path = tk_utils.get_path()
    tk_utils.are_you_sure(path)
    validation.check_structure(path)
    routine.run(path)