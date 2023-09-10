#función para separar el dataset en X - y
from functions_methods.utils import load_data, X_y_separation

from models_metrics.MLmodels import test

import pickle


def model_testing():
    '''
    Esta función toma el archivo test.csv que se separó al principio,
    le aplica la transformación (pipeline) a la matrix X, predice la y con el modelo
    y luego evalúa las métricas con la función test()
    '''
    test_file = load_data('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/test.csv')

    X_test, y_test = X_y_separation(test_file, 'satisfaction')

    with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/pipeline.pkl', 'rb') as archivo:
        pipeline = pickle.load(archivo)
    
    X_test_transformed = pipeline.transform(X_test)
    
    with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/catboost_airplanes.pkl', 'rb') as archivo:
        model = pickle.load(archivo)
        
    y_predicted = model.predict(X_test_transformed)

    test(y_predicted, y_test)


def one_prediction(data_to_predict):
    '''
    Esta función recibe un sólo registro de la matriz X.
    Predice con el modelo y devuelve 'satisfied' o 'neutral or dissatisfied'
    '''
    one_register = load_data()
    
    with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/pipeline.pkl', 'rb') as archivo:
        pipeline = pickle.load(archivo)
    
    X_transformed = pipeline.transform(data_to_predict)
    
    with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/catboost_airplanes.pkl', 'rb') as archivo:
        model = pickle.load(archivo)
        
    y_predicted = model.predict(X_transformed)

    print(y_predicted)