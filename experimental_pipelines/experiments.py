#librería de manejo de datos
import pandas as pd

#librería para hacer pipeline
from sklearn.pipeline import Pipeline

#librerías para escalar
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#importamos el módulo creado y las librerías para transformar el dataset 
from sklearn.compose import ColumnTransformer
import functions_methods.custom_transformers

from sklearn.pipeline import Pipeline

# # Crear instancias de los transformadores personalizados
# drop_rows_transformer = DropRowsTransformer()
# drop_columns_transformer = DropColumnsTransformer(list_cols_to_drop=['column_to_drop'])
# simple_imputer_transformer = SimpleImputerTransformer(string_strategy='mean')
# onehot_labelencoder_transformer = OneHotLabelEncoderTransformer(drop='if_binary')

# # Crear un pipeline con los transformadores
# pipeline = Pipeline([
#     ('drop_rows', drop_rows_transformer),
#     ('drop_columns', drop_columns_transformer),
#     ('simple_imputer', simple_imputer_transformer),
#     ('onehot_labelencoder', onehot_labelencoder_transformer),
# ])

# # Ajustar el pipeline y transformar los datos
# X_transformed, y_transformed = pipeline.fit_transform(X, y)
