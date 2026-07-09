import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl') # Just a path string on disk nothing is created on disk here — only when save_object() is called



class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig() # stores config object in self. so all methods can access the path



    def get_data_transformation_object(self):  # builds and returns the ColumnTransformer (preprocessor blueprint),does NOT apply anything to data yet — just defines the steps

        try:
            numerical_columns = ['writing_score', 'reading_score']
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]
            # math_score is NOT here — it is the target, not an input feature

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),# fills missing numbers with median of that column,median chosen over mean — not affected by outliers
                    ("scaler", StandardScaler())  # scales numbers to mean=0, std=1, prevents large-valued columns dominating the model

                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")), # fills missing text with most common value in that column
                    ("one_hot_encoder", OneHotEncoder()), # converts text categories to binary columns,e.g. gender: female→[1,0]  male→[0,1]
                    ("scaler", StandardScaler(with_mean=False)) # with_mean=False → does NOT subtract mean, subtracting mean (with_mean=True) destroys sparse structure → memory issues

                ]
            )

            logging.info(f'Categorical columns: {categorical_columns}')
            logging.info(f'Numerical columns: {numerical_columns}')

            preprocessor = ColumnTransformer(  # combines both outputs into one single array automatically
                [
                    ('num_pipeline', num_pipeline, numerical_columns), # applies num_pipeline to numerical columns
                    ('cat_pipeline', cat_pipeline, categorical_columns) # applies cat_pipeline to categorical columns
                ]
            )
  
    
            return preprocessor # returns the ColumnTransformer object — not yet fitted, just built

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path): # train_path, test_path received from DataIngestion,  e.g. 'artifacts/train.csv', 'artifacts/test.csv'
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessor_obj = self.get_data_transformation_object()
      

            target_column_name = 'math_score'
          

            # ── split features and target ──
            input_feature_train_df  = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]
       

            input_feature_test_df  = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                "Applying preprocessing object on training dataframe and testing dataframe."
            )

   
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
    

            train_arr = np.c_[  # np.c_[] joins two arrays horizontally column by column, e.g. esult: [features... | math_score]  (800 rows, 8 cols)
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
        
         
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            # same operation for test data (200 rows, 8 cols)

            logging.info('Saved preprocessing object.')

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,  # file_path → 'artifacts/preprocessor.pkl'  WHERE to save (just a string)
                obj=preprocessor_obj  # obj → preprocessor_obj → WHAT to save (the actual object)
            )
            # self.data_transformation_config  → the config object
            # self.data_transformation_config.preprocessor_obj_file_path → the path string INSIDE it
            # why save? → reuse same preprocessor during prediction without retraining it

            # returns tuple passed to ModelTrainer:
            return (
                train_arr, # train_arr  → transformed training data (features + target)
                test_arr,  # test_arr   → transformed test data     (features + target)
                self.data_transformation_config.preprocessor_obj_file_path # .pkl path  → preprocessor location for prediction pipeline

            )
            # returns tuple passed to ModelTrainer:
        
      

        except Exception as e:
            raise CustomException(e, sys)
