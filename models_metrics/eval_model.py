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

df = load_data()

X_train, y_train = X_y_separation(df, 'satisfaction')

def transform_data(X, y_true):

    cols_to_drop = ['unnamed', 'id', 'arrival_delay', 'departure_delay', 'gender', 'departure_arrival_time']
    strategy = 'median'
    drop_onehot = 'first'
    limit_short = 1300
    limit_medium = 2000
    add_flight_cat = False

    #creamos la nueva columna de distancia de vuelo categórica según el booleano add_flight_cat
    if add_flight_cat:
        data_to_predict = CategoricalDistance(limit_short = limit_short, limit_medium = limit_medium).transform(X)
    else:
        data_to_predict = X
    
    #creamos un pipeline con los transformadores
    X_numeric = data_to_predict.select_dtypes(include = ['number'])
    num_columns = list(X_numeric)

    X_categorical = data_to_predict.select_dtypes(include = ['object'])
    cat_columns = list(X_categorical)

    num_pipeline = Pipeline([('imputer', SimpleImputer(strategy = strategy)),
                             ('minmaxscaler', MinMaxScaler())])

    full_pipeline = ColumnTransformer([('drop_col', 'drop', cols_to_drop),
                                       ('num', num_pipeline, num_columns),
                                       ('cat', OneHotEncoder(drop = drop_onehot), cat_columns)],
                                       remainder = 'passthrough')
   
    #ajustamos el pipeline y transformamos los datos
    X_transformed = full_pipeline.fit_transform(data_to_predict)
    y_transformed = LabelEncoder().fit_transform(y_true)
    
    return X_transformed, y_transformed


