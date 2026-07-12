import os 
import sys 

import numpy as np 
import pandas as pd 
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path) # 'artifacts/preprocessor.pkl' → 'artifacts'

        os.makedirs(dir_path, exist_ok=True) # creates artifacts/ folder if it doesn't exist

        with open(file_path, mode='wb') as file_obj:
            dill.dump(obj,file_obj)
        #  dill.dump() does two things:
        #   1. converts Python object → bytes
        #   2. writes bytes into the .pkl file

    except Exception as e:
        raise CustomException(e,sys)
            



def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
            
            # Train and evaluate each model
        for name,model in models.items():

                # Get hyperparameters for the current model
                para = param[name]

                # Perform Grid Search to find the best hyperparameters
                gs = GridSearchCV(model,para,cv=3)
                gs.fit(X_train, y_train)


                # Update model with best hyperparameters
                # e.g. RandomForestRegressor(n_estimators=64)
                # Notice: This line does not train the model. It only changes its parameter values.

                model.set_params(**gs.best_params_)

                # Train the model again using the best parameters
                # This trains the original model, but using the best hyperparameters found by GridSearchCV.
                model.fit(X_train, y_train)

                # Predictions
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)

                # Calculate R² scores
                train_model_score = r2_score(y_train, y_train_pred)
                test_model_score = r2_score(y_test, y_test_pred)



                # Store only the test R² score
                report[name] = test_model_score
                
        return report


    except Exception as e:
            raise CustomException(e,sys)


def load_object(file_path):
    try:
        with open(file_path, mode='rb') as file_obj:
            return pickle.load(file_obj)
        

    except Exception as e:
        raise CustomException(e, sys)