import logging
from datetime import datetime

class Log:
    def __init__(self):
        self.now = datetime.now().strftime("%H-%M-%S")
        self.name = "output-" + self.now + ".log"
    def create(self):
        logging.basicConfig(filename=self.name, format='%(asctime)s %(message)s', filemode='w')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        return self.logger

logger = Log().create()