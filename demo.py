from src import logger
from src.exception import MyException
import sys
logger.logging.debug("This is a Debug message")

try: 
    a = 1+'a'
except Exception as e:
    logger.logging.error(e)
    raise MyException(e,sys) from e