import src.tk as tk
import src.validation as validation
import src.routine as routine

if(__name__ == '__main__'):
    path = tk.get_path()
    validation.confirm_processing(path)
    validation.check_structure(path)
    routine.run(path)