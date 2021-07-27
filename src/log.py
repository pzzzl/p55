import logging
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H-%M-%S")
output_log_name = "output-" + current_time + ".log"

logging.basicConfig(filename=output_log_name, format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.INFO)