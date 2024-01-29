from src.Unsupervised_end_to_end_Project.logger import logging
from src.Unsupervised_end_to_end_Project.exception import CustomException
import sys




if __name__ == "__main__":
    logging.info("This is a test log message")
    try:
        a = 1/0
    except Exception as e: 
        logging.info("Exception occured")   
        raise CustomException(e, sys)