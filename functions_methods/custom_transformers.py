#librería de manejo de datos
import pandas as pd

#librerías para imputar nulos
from sklearn.impute import SimpleImputer

#librerías para codificar variables categóricas
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

#librerías para crear custom transformers
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import FunctionTransformer


#LLENADO/ELIMINACIÓN DE NULOS

class DropRowsTransformer(BaseEstimator, TransformerMixin):
    '''
    Elimina las filas que tienen nulos.
    '''
    def __init__(self):
        pass

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        return X.dropna(axis = 0)


class DropColumnsTransformer(BaseEstimator, TransformerMixin):
    '''
    Recibe el dataframe y la lista de columnas que se quieren eliminar.
    Devuelve el dataframe modificado.
    '''
    def __init__(self, list_cols_to_drop):
        self.list_cols_to_drop = list_cols_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(self.list_cols_to_drop, axis = 1)


class SimpleImputerTransformer(BaseEstimator, TransformerMixin):
    '''
    Recibe el dataframe completo y la estrategia para imputar como string.
    Devuelve el dataframe completo sin nulos numéricos aplicando
    la estrategia pasada como parámetro.
    '''
    def __init__(self, string_strategy):
        self.string_strategy = string_strategy

    def fit(self, X, y = None):
        self.imputer = SimpleImputer(strategy = self.string_strategy)
        self.imputer.fit(X.select_dtypes(include = ['number']))
        return self

    def transform(self, X):
        df_numeric = X.select_dtypes(include = ['number'])
        X_imputed = self.imputer.transform(df_numeric)
        df_no_numeric = X.select_dtypes(exclude = ['number'])
        df_numeric = pd.DataFrame(X_imputed, columns = df_numeric.columns)
        return pd.concat([df_no_numeric, df_numeric], axis = 1)


#CODIFICACIÓN DE VARIABLES CATEGÓRICAS

class OneHotLabelEncoderTransformer(BaseEstimator, TransformerMixin):
    '''
    Recibe la matriz X, el vector de salida y, y el parámetro drop del OneHotEncoder().
    Devuelve la matriz X y el vector y codificados.
    '''
    def __init__(self, drop = 'if_binary'):
        self.drop = drop

    def fit(self, X, y = None):
        self.encoder1 = OneHotEncoder(drop = self.drop)
        self.encoder1.fit(X.select_dtypes(include = ['object']))

        self.encoder2 = LabelEncoder()
        self.encoder2.fit(y)
        return self

    def transform(self, X, y = None):
        X_categorical = X.select_dtypes(include = ['object'])
        X_encoded = self.encoder1.transform(X_categorical)

        y_encoded = self.encoder2.transform(y)

        return X_encoded, y_encoded


#TRANSFORMACIÓN DE LA VARIABLE DISTANCIA DE VUELO

class CategoricalDistance(BaseEstimator, TransformerMixin):
    '''
    Esta clase transforma la columna numérica distancia de vuelo en categórica
    '''
    def __init__(self, limit_short, limit_medium):
        self.limit_short = int(limit_short)
        self.limit_medium = int(limit_medium)
    
    def fit(self, X, y = None):
        return self
       
    def transform(self, X):  
        #hacemos una copia del DataFrame de entrada
        X_copy = X.copy()

        #creamos la columna 'flight_distance_cat' basada en la distancia de vuelo
        X_copy['flight_distance_cat'] = 'short'

        #establecemos 'short' para vuelos cortos
        X_copy.loc[X_copy['flight_distance'] <= self.limit_short, 'flight_distance_cat'] = 'short'

        #establecemos 'medium' para vuelos entre limit_short y limit_medium
        X_copy.loc[(X_copy['flight_distance'] > self.limit_short) & (X_copy['flight_distance'] <= self.limit_medium), 'flight_distance_cat'] = 'medium'

        #long para vuelos largos
        X_copy.loc[X_copy['flight_distance'] > self.limit_medium, 'flight_distance_cat'] = 'long'

        return X_copy
