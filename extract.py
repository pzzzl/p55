import os
import sys
import src.args as args
import src.validation as validation
import src.routine as routine
from shutil import move

if(__name__ == '__main__'):
    path = args.verify_path()
    validation.confirm_processing(path)
    validation.check_structure(path)
    routine.run(path)
