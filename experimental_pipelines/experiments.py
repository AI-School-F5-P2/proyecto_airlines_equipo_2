#librería de manejo de datos
import pandas as pd
import numpy as np

#librería para hacer pipeline
from sklearn.pipeline import Pipeline

#importamos el módulo creado y las librerías para transformar el dataset 
from sklearn.compose import ColumnTransformer
from functions_methods.custom_transformers import DropColumnsTransformer, DropRowsTransformer, CategoricalDistance 
from functions_methods.custom_transformers import SimpleImputerTransformer, OneHotEncoderTransformer, LabelEncoderTransformer
from functions_methods.custom_transformers import MinMaxScalerTransformer


def experiment(X_train, y_train, cols_to_drop, strategy, drop_onehot, limit_short, limit_medium):
    '''
    Esta función recibe el dataframe de train dividido en 2: X_train, y_train.
    Devuelve la X_train transformada y la y_train con label encoder aplicado
    '''
    #creamos instancias de los transformadores personalizados
    drop_rows = DropRowsTransformer()
    drop_columns = DropColumnsTransformer(list_cols_to_drop = cols_to_drop)
    simple_imputer = SimpleImputerTransformer(string_strategy = strategy)
    onehot_encoder = OneHotEncoderTransformer(drop = drop_onehot)
    flight_categorical = CategoricalDistance(limit_short = limit_short, limit_medium = limit_medium)
    minmax = MinMaxScalerTransformer()
    label_encoder = LabelEncoderTransformer()

    X_train.drop(X_train.columns[X_train.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    #creamos un pipeline con los transformadores
    pipeline_X = ColumnTransformer([('drop_rows', drop_rows),
                                ('drop_columns', drop_columns),
                                ('simple_imputer', simple_imputer),
                                ('flight_categorical', flight_categorical),
                                ('onehot_encoder', onehot_encoder),
                                ('minmax', minmax)], remainder = 'passthrough')
    print(pipeline_X)
    print(X_train.head())
    print(y_train.head())
    #ajustar el pipeline y transformar los datos
    X_transformed = pipeline_X.fit_transform(X_train)
    y_transformed = label_encoder.fit_transform(y_train)
    return X_transformed, y_transformed

def first_experiment(X_train, y_train):
    #columnas sobre las que se quiere aplicar cierta transformación
    cols_to_drop_1 = ['arrival_delay', 'unnamed']
    strategy_1 = 'median'
    drop_onehot_1 = 'first'
    limit_short_1 = 1300
    limit_medium_1 = 2000

    X_transformed1, y_transformed1 = experiment(X_train, y_train, cols_to_drop_1, strategy_1, drop_onehot_1, 
                                                limit_short_1, limit_medium_1)
    return X_transformed1, y_transformed1
