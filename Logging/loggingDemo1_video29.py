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

logging.basicConfig(filename="test.log", format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p', level=logging.DEBUG)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

