###################### Logging and log levels ####################
# Logging is a very useful tool in a programmer's toolbox. It can help you develop a
# better understanding of the flow of a program and discover scenarios that you might
# not even have thought of while developing.

##### Log Levels #######
#     1. DEBUG
#     2. INFO
#     3. WARNING
#     4. ERROR
#     5. CRITICAL


import logging

logging.basicConfig(filename="test2.log", format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p', level=logging.DEBUG)

# Creating logger object   ( the best way)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
