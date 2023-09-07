#librería de manejo de datos
import pandas as pd

#librerías para imputar nulos
from sklearn.impute import SimpleImputer

#librerías para codificar variables categóricas
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler

#librerías para crear custom transformers
from sklearn.base import BaseEstimator, TransformerMixin


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
        return (X.dropna(axis = 0)).values


class DropColumnsTransformer(BaseEstimator, TransformerMixin):
    '''
    Recibe el dataframe y la lista de columnas que se quieren eliminar.
    Devuelve el dataframe modificado.
    '''
    def __init__(self, list_cols_to_drop):
        self.list_cols_to_drop = list_cols_to_drop

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        return (X.drop(self.list_cols_to_drop, axis = 1)).values


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
        return (pd.concat([df_no_numeric, df_numeric], axis = 1)).values


#CODIFICACIÓN DE VARIABLES CATEGÓRICAS

class OneHotEncoderTransformer(BaseEstimator, TransformerMixin):
    '''
    Recibe la matriz X y el parámetro drop del OneHotEncoder().
    Devuelve la matriz X codificada.
    '''
    def __init__(self, drop = 'if_binary'):
        self.drop = drop

    def fit(self, X, y = None):
        self.encoder = OneHotEncoder(drop = self.drop)
        self.encoder.fit(X.select_dtypes(include = ['object']))
        return self

    def transform(self, X, y = None):
        X_categorical = X.select_dtypes(include = ['object'])
        X_encoded = self.encoder.transform(X_categorical)
        print(X_encoded)
        return X_encoded.values


class LabelEncoderTransformer(BaseEstimator, TransformerMixin):
    '''
    Recibe el vector y de salida.
    Devuelve la variable codificada con 0 y 1.
    '''
    def __init__(self):
        pass

    def fit(self, y):
        self.encoder = LabelEncoder()
        self.encoder.fit(y)
        return self

    def transform(self, y):
        y_encoded = self.encoder.transform(y)
        return y_encoded.values


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

        return X_copy.values


class MinMaxScalerTransformer(BaseEstimator, TransformerMixin):
    '''
    Recibe la matriz X y opcionalmente los parámetros feature_range y clip del MinMaxScaler.
    Devuelve la matriz X escalada.
    '''
    def __init__(self, feature_range = (0, 1), clip = False):
        self.feature_range = feature_range
        self.clip = clip

    def fit(self, X, y = None):
        self.scaler = MinMaxScaler(feature_range = self.feature_range, clip = self.clip)
        self.scaler.fit(X.select_dtypes(include = ['number']))
        return self

    def transform(self, X, y = None):
        X_numeric = X.select_dtypes(include = ['number'])
        X_scaled = self.scaler.transform(X_numeric)
        return X_scaled.values
