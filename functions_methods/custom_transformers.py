#librería de manejo de datos
import pandas as pd

#librerías para imputar nulos
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

#librerías para codificar variables categóricas
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

#librerías para crear custom transformers
from sklearn.base import BaseEstimator, TransformerMixin

#LLENADO DE NULOS

def drop_rows(df):
    '''
    Elimina las filas que tienen nulos.
    '''
    df.dropna(axis = 0, inplace = True)
    return df


def drop_columns(df, list_cols_to_drop):
    '''
    Recibe el dataframe y la lista de columnas que se quieren eliminar.
    Devuelve el dataframe modificado.
    '''
    df.drop(list_cols_to_drop, axis = 1, inplace = True)
    return df


def simple_imputer(df, string_strategy):
    '''
    Recibe el dataframe completo y la estrategia para imputar como string.
    Devuelve el dataframe completo sin nulos numéricos aplicando
    la estrategia pasada como parámetro.
    '''
    #instanciamos el SimpleImputer con la estrategia pasada como parámetro
    imputer = SimpleImputer(strategy = string_strategy)

    #filtramos sólo las columnas numéricas para que la strategy funcione
    df_numeric = df.select_dtypes(include = ['number'])

    X = imputer.fit_transform(df_numeric)

    #concatenamos df_numeric con las columnas no numéricas del dataframe original
    df_no_numeric = df.select_dtypes(exclude = ['number'])
    df_numeric = pd.DataFrame(X, columns = df_numeric.columns)
    df = pd.concat([df_no_numeric, df_numeric], axis = 1)
    return df


#CODIFICACIÓN DE VARIABLES CATEGÓRICAS

def onehot_X_label_y(X, y, drop = 'if_binary'):
    '''
    Recibe la matriz X, el vector de salida y, y el parámetro drop del OneHotEncoder().
    Devuelve la matriz X y el vector y codificados.
    '''
    X_categorical = X.select_dtypes(include = ['object'])
    encoder1 = OneHotEncoder(drop = drop)
    X_encoded = encoder1.fit_transform(X_categorical)

    encoder2 = LabelEncoder()
    y_encoded = encoder2.fit_transform(y)

    return X_encoded, y_encoded


#CUSTOM TRANSFORMERS

class CategoricalDistance(BaseEstimator, TransformerMixin):
    pass
    #def __init__(self, limit_short_medium):
        #self.limit_short_medium = limit_short_medium
    #def fit(self, X, y = None):
        #return self
    #def transform(self, X):
        #if x <= 1500:
            #return 'short'
        #elif 1500 < x <= 3000:
            #return 'medium'
        #else:
            #return 'long'

#df_air_transformed['flight_distance_cat'] = df_air_transformed.flight_distance.apply(categorize_distance)