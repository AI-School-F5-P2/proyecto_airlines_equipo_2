#librería de manejo de datos
import pandas as pd

#librería para hacer pipeline
from sklearn.pipeline import Pipeline

#librerías para escalar
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#importamos el módulo creado y las librerías para transformar el dataset 
from sklearn.compose import ColumnTransformer
from functions_methods.custom_transformers import DropColumnsTransformer, DropRowsTransformer, CategoricalDistance 
from functions_methods.custom_transformers import SimpleImputerTransformer, OneHotLabelEncoderTransformer

def experiments():
    '''
    Esta función recibe el dataframe de train dividido en 2: X_train, y_train.
    Devuelve la X_train transformada y la y_train con label encoder aplicado
    '''
    #columnas sobre las que se quiere aplicar cierta transformación
    cols_to_drop = []
    cols_numeric = []
    cols_categorical = []
    y_output = []

    #creamos instancias de los transformadores personalizados
    drop_rows = DropRowsTransformer()
    drop_columns = DropColumnsTransformer(list_cols_to_drop = cols_to_drop)
    simple_imputer = SimpleImputerTransformer(string_strategy = 'mean')
    onehot_labelencoder = OneHotLabelEncoderTransformer(drop = 'if_binary')
    flight_categorical = CategoricalDistance(limit_short = 1500, limit_medium = 3000)
    minmax = MinMaxScaler()
    standard = StandardScaler()

    #creamos un pipeline con los transformadores
    pipeline = ColumnTransformer([('drop_rows', drop_rows),
                                ('drop_columns', drop_columns),
                                ('simple_imputer', simple_imputer, cols_numeric),
                                ('onehot_labelencoder', onehot_labelencoder),
                                ('flight_categorical', flight_categorical)
                                ('minmax', minmax, cols_numeric)])
    
    #ajustar el pipeline y transformar los datos
    #X_transformed, y_transformed = pipeline.fit_transform(X, y)
    #return X_transformed, y_transformed
