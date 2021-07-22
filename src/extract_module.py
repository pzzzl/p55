from src.tk_utils import Utils
import src.validation as validation
import src.routine as routine

# remover as instâncias do tk sendo passadas
def extract():
    Utils().start()
    path = Utils().get_path()
    Utils().are_you_sure(path)
    validation.check_structure(path)
    routine.run(path)