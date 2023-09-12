import pandas as pd

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
    test_file = load_data('test.csv')

    X_test, y_test = X_y_separation(test_file, 'satisfaction')

    with open('pipeline.pkl', 'rb') as archivo:
        pipeline = pickle.load(archivo)
    
    X_test_transformed = pipeline.transform(X_test)
    
    with open('catboost_airplanes.pkl', 'rb') as archivo:
        model = pickle.load(archivo)
        
    y_predicted = model.predict(X_test_transformed)

    test(y_predicted, y_test)


def load_data_to_predict(path_to_data):
    '''
    Lee los datos de un archivo csv y modifica los nombres de las columnas
    para usarlas más fácilmente.
    '''
    try:
        #reescribo el nombre de las columnas para poder acceder a ellas más fácilmente
        name_cols = {'Unnamed': 'unnamed',
                     'id': 'id',
                     'Gender': 'gender',
                     'Customer Type': 'customer_type',
                     'Age': 'age',
                     'Type of Travel': 'type_travel',
                     'Class': 'clase',
                     'Flight Distance': 'flight_distance',
                     'Inflight wifi service': 'wifi_service',
                     'Departure/Arrival time convenient': 'departure_arrival_time',
                     'Ease of Online booking': 'online_booking',
                     'Gate location': 'gate_location',
                     'Food and drink': 'food_drink',
                     'Online boarding': 'online_boarding',
                     'Seat comfort': 'seat_comfort',
                     'Inflight entertainment': 'entertain',
                     'On-board service': 'onboard_service',
                     'Leg room service': 'leg_service',
                     'Baggage handling': 'bag_handle',
                     'Checkin service': 'checkin_service',
                     'Inflight service': 'inflight_service',
                     'Cleanliness': 'cleanliness',
                     'Departure Delay in Minutes': 'departure_delay',
                     'Arrival Delay in Minutes': 'arrival_delay'}

        #formato lista para poder pasarlas como parámetro names
        name_cols = list(name_cols.values())

        #creación del dataframe
        df = pd.read_csv(path_to_data, header = 0, names = name_cols)
        return df
    
    except FileNotFoundError:
        print(f"El archivo no se encontró.")
        return None
    
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {str(e)}")
        return None


def one_prediction():
    '''
    Esta función recibe un sólo registro de la matriz X.
    Predice con el modelo y devuelve 'satisfied' o 'neutral or dissatisfied'
    '''
    X_to_predict = load_data_to_predict('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/one_register.csv')
    
    with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/pipeline.pkl', 'rb') as archivo:
        pipeline = pickle.load(archivo)
    
    X_transformed = pipeline.transform(X_to_predict)
    
    with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/catboost_airplanes.pkl', 'rb') as archivo:
        model = pickle.load(archivo)
        
    y_predicted = model.predict(X_transformed)

    print(y_predicted)