import os 
import sys 

import numpy as np 
import pandas as pd 
import dill
import pickle
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
            