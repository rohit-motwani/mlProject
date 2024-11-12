import sys
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.mlProject.logger import logging
from src.mlProject.exception import CustomeException
from src.mlProject.utils import save_object
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransfromation:
    def __init__(self):
        self.data_tranformation_config = DataTransformationConfig()
        
    def get_transformer_object(self):
        '''
        this function is responsible for data transformation        
        '''
        try:
            numerical_columns = ["writing_score","reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ('scalar',StandardScaler())
            ])
            cat_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder',OneHotEncoder()),
                ('scalar',StandardScaler(with_mean=False))
            ])
            
            logging.info(f"Categorical column: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            
            return preprocessor
        
        except Exception as e:
            raise CustomeException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Reading the train and test file")
            
            preprocessing_obj=self.get_transformer_object()
            
            target_column_name="math_score"
            numerical_columns = ["writing_score","reading_score"]
            
            input_features_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            input_features_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            logging.info("Applying preprocessing on training and testing datafrane")
            
            input_featur_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_featur_test_arr = preprocessing_obj.transform(input_features_test_df)
            
            train_arr = np.c_[
                input_featur_train_arr,np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_featur_test_arr,np.array(target_feature_test_df)
            ]
            logging.info(f"Saved succesfully")
            
            save_object(
                file_path=self.data_tranformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            return(
                train_arr,
                test_arr,
                self.data_tranformation_config.preprocessor_obj_file_path
            )
            
        except Exception as e:
            raise CustomeException(e,sys)