#librería de manejo de datos
import pandas as pd
import numpy as np

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
from functions_methods.utils import X_y_separation

import pickle


def experiment(X_train, y_train, cols_to_drop, strategy, drop_onehot, limit_short, limit_medium, add_flight_cat):
    '''
    Esta función recibe el dataframe de train dividido en 2: X_train, y_train.
    Devuelve la X_train transformada y la y_train con label encoder aplicado
    '''
    #creamos la nueva columna de distancia de vuelo categórica según el booleano add_flight_cat
    if add_flight_cat:
        X_train_add = CategoricalDistance(limit_short = limit_short, limit_medium = limit_medium).transform(X_train)
    else:
        X_train_add = X_train
    
    #creamos un pipeline con los transformadores
    X_numeric = X_train_add.select_dtypes(include = ['number'])
    num_columns = list(X_numeric)

    X_categorical = X_train_add.select_dtypes(include = ['object'])
    cat_columns = list(X_categorical)

    num_pipeline = Pipeline([('imputer', SimpleImputer(strategy = strategy)),
                             ('minmaxscaler', MinMaxScaler())])

    full_pipeline = ColumnTransformer([('drop_col', 'drop', cols_to_drop),
                                       ('num', num_pipeline, num_columns),
                                       ('cat', OneHotEncoder(drop = drop_onehot), cat_columns)],
                                       remainder = 'passthrough')
   
    #ajustamos el pipeline y transformamos los datos
    X_transformed = full_pipeline.fit_transform(X_train_add)
    y_transformed = LabelEncoder().fit_transform(y_train)
    
    return X_transformed, y_transformed

def first_experiment(X_train, y_train):
    '''
    En este tipo de funciones exploramos diferentes transformaciones 
    para identificar la mejor combinación de estas
    '''
    #columnas sobre las que se quiere aplicar cierta transformación
    cols_to_drop_1 = ['unnamed']
    strategy_1 = 'median'
    drop_onehot_1 = 'first'
    limit_short_1 = 1500
    limit_medium_1 = 3000
    add_flight_cat1 = False

    X_transformed1, y_transformed1 = experiment(X_train, y_train, cols_to_drop_1, strategy_1, 
                                                drop_onehot_1, limit_short_1, limit_medium_1, 
                                                add_flight_cat1)
    return X_transformed1, y_transformed1

def second_experiment(X_train, y_train):

    cols_to_drop_2 = ['unnamed', 'id', 'departure_delay']
    strategy_2 = 'median'
    drop_onehot_2 = 'first'
    limit_short_2 = 1300
    limit_medium_2 = 2000
    add_flight_cat2 = False

    X_transformed2, y_transformed2 = experiment(X_train, y_train, cols_to_drop_2, strategy_2,
                                                drop_onehot_2, limit_short_2, limit_medium_2, 
                                                add_flight_cat2)
    return X_transformed2, y_transformed2
  

def third_experiment(X_train, y_train):

    cols_to_drop_3 = ['unnamed', 'id', 'arrival_delay', 'departure_delay', 'gender', 'departure_arrival_time']
    strategy_3 = 'median'
    drop_onehot_3 = 'first'
    limit_short_3 = 1300
    limit_medium_3 = 2000
    add_flight_cat3 = False

    X_transformed3, y_transformed3 = experiment(X_train, y_train, cols_to_drop_3, strategy_3,
                                                drop_onehot_3, limit_short_3, limit_medium_3, 
                                                add_flight_cat3)
    return X_transformed3, y_transformed3
  
def fourth_experiment(X_train, y_train):

    cols_to_drop_4 = ['unnamed', 'id', 'arrival_delay', 'departure_delay', 'gender', 'departure_arrival_time']
    strategy_4 = 'median'
    drop_onehot_4 = 'first'
    limit_short_4 = 1300
    limit_medium_4 = 2000
    add_flight_cat4 = True

    X_transformed4, y_transformed4 = experiment(X_train, y_train, cols_to_drop_4, strategy_4,
                                                drop_onehot_4, limit_short_4, limit_medium_4, 
                                                add_flight_cat4)
    return X_transformed4, y_transformed4

def fifth_experiment(X_train, y_train):

    cols_to_cat = ['wifi_service', 'departure_arrival_time', 'online_booking', 'gate_location', 'food_drink', 
                   'online_boarding', 'seat_comfort', 'entertain', 'onboard_service', 'leg_service', 'bag_handle', 
                   'checkin_service', 'inflight_service', 'cleanliness']

    X_train[cols_to_cat] = X_train[cols_to_cat].astype('object')
 
    cols_to_drop_5 = ['unnamed', 'id', 'arrival_delay']
    strategy_5 = 'median'
    drop_onehot_5 = 'first'
    limit_short_5 = 1300
    limit_medium_5 = 2000
    add_flight_cat5 = True

    X_transformed5, y_transformed5 = experiment(X_train, y_train, cols_to_drop_5, strategy_5,
                                                drop_onehot_5, limit_short_5, limit_medium_5, 
                                                add_flight_cat5)
    return X_transformed5, y_transformed5
  
def sixth_experiment(X_train, y_train):

    #concatenamos primero para que se modifique el registro entero
    complete_df = pd.concat([X_train, y_train], axis = 1)

    complete_df = complete_df.dropna()
 
    X_train, y_train = X_y_separation(complete_df, 'satisfaction')

    cols_to_drop_6 = ['unnamed', 'id', 'arrival_delay', 'departure_delay', 'gender', 'departure_arrival_time']
    strategy_6 = 'median'
    drop_onehot_6 = 'first'
    limit_short_6 = 1300
    limit_medium_6 = 2000
    add_flight_cat6 = True

    X_transformed6, y_transformed6 = experiment(X_train, y_train, cols_to_drop_6, strategy_6,
                                                drop_onehot_6, limit_short_6, limit_medium_6, 
                                                add_flight_cat6)
    return X_transformed6, y_transformed6

def seventh_experiment(X_train, y_train):

    cols_to_drop_7 = ['unnamed', 'id', 'arrival_delay', 'departure_delay', 'gender', 'departure_arrival_time']
    strategy_7 = 'median'
    drop_onehot_7 = 'first'
    limit_short_7 = 1500
    limit_medium_7 = 3000
    add_flight_cat7 = True

    X_transformed7, y_transformed7 = experiment(X_train, y_train, cols_to_drop_7, strategy_7,
                                                drop_onehot_7, limit_short_7, limit_medium_7, 
                                                add_flight_cat7)
    return X_transformed7, y_transformed7