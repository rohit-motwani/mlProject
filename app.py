from src.mlProject.logger import logging
from src.mlProject.exception import CustomeException
import sys
from src.mlProject.components.data_ingestion import DataIngestion
from src.mlProject.components.data_ingestion import DataIngestionConfig
from src.mlProject.components.data_transformation import DataTransformationConfig,DataTransfromation

if __name__ == "__main__":
    logging.info("The execution has started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        
        data_tranformation = DataTransfromation()
        data_tranformation.initiate_data_transformation(train_data_path,test_data_path)
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomeException(e,sys)