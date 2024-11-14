import os
import sys
from src.mlProject.exception import CustomeException
from src.mlProject.logger import logging
import pandas as pd
from src.mlProject.utils import read_sql_data
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.mlProject.components.data_transformation import DataTransformationConfig,DataTransfromation
from src.mlProject.components.model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv(os.path.join('notebook','raw.csv'))
            logging.info("Reading from Mysql Database")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Data Ingestion is Completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomeException(e,sys)
        
# if __name__=="__main":
#     data_ingestion = DataIngestion()
#     train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        
#     data_tranformation = DataTransfromation()
#     train_arr,test_arr,_ = data_tranformation.initiate_data_transformation(train_data_path,test_data_path)
        
#     model_trainer = ModelTrainer()
#     print(model_trainer.initiate_model_trainer(train_arr,test_arr))