from src.mlProject.logger import logging
from src.mlProject.exception import CustomeException
import sys

if __name__ == "__main__":
    logging.info("The execution has started")
    
    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomeException(e,sys)