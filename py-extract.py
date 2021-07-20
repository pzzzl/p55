import src.tk as tk
import src.validation as validation
import src.routine as routine

if(__name__ == '__main__'):
    tk.start()
    path = tk.get_path()
    tk.are_you_sure(path)
    validation.check_structure(path)
    routine.run(path)