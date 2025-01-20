import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime


LOG_DIR ="logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024 #5MB
BACKUP_COUNT = 3 # Numnber of backup log files to keep

#Setting up log file path
log_dir_path = os.path.join(from_root(),LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path = os.path.join(log_dir_path,LOG_FILE)


def configure_logger():
    """ 
    Config log with the rotating file handler and console handler
    """

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # formatter 
    formatter = logging.Formatter("[%(asctime)s - %(name)s - %(levelname)s - %(message)s]")
    
    #file_handler
    file_handler = RotatingFileHandler(log_file_path,maxBytes=MAX_LOG_SIZE,backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    #console_handler 
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

configure_logger()



