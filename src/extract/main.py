from src.tk_utils import Utils
import src.validation as validation
import src.extract.routine as routine

def extract():
    Utils().start(msg='Choose the directory tree which will have all files extracted to a single folder "extracted".')
    path = Utils().get_path()
    Utils().are_you_sure(msg='Are you sure you want to extract all files from the folder "' + path + '" into a single folder "extracted"?')
    validation.check_structure(path, "extracted")
    routine.run(path)