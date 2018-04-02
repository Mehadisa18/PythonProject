# Log levels:
# UNSET - 0
# DEBUG - 10
# INFO - 20
# WARNING - 30 # default 
# ERROR - 40
# CRITICAL - 60

import logging 

logformat = " %(levelname)s %(asctime)s - %(message)s "
logging.basicConfig(filename="logfile", level = logging.DEBUG,
 format=logformat , filemode='w') # write mode is opposite of append mode. A fresh copy is created everytime
logger = logging.getLogger()
logger.debug('Warning msg')
