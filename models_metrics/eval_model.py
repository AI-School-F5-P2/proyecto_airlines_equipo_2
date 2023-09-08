#librería para hacer pipeline
from sklearn.pipeline import Pipeline

#importamos el módulo creado y las librerías para transformar el dataset 
from sklearn.compose import ColumnTransformer
from functions_methods.custom_transformers import CategoricalDistance 

#librerías para imputar nulos
from sklearn.impute import SimpleImputer

#librerías para codificar variables
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler

#función para separar el dataset en X - y
from functions_methods.utils import load_data, X_y_separation

from models_metrics.MLmodels import test

import pickle


def model_testing():

    test_file = load_data('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/test.csv')

    X_test, y_test = X_y_separation(test_file, 'satisfaction')

    with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/pipeline.pkl', 'rb') as archivo:
        pipeline = pickle.load(archivo)
    
    X_test_transformed = pipeline.transform(X_test)
    
    y_test_transformed = LabelEncoder().transform(y_test)

    with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/catboost_airplanes.pkl', 'rb') as archivo:
        model = pickle.load(archivo)
        
    y_predicted = model.predict(X_test_transformed)

    test(y_predicted, y_test_transformed)