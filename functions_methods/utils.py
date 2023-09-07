#librería de manejo de datos
import pandas as pd

#librería para separar los sets de train y test
from sklearn.model_selection import train_test_split


def load_data():
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
                     'Class': 'class',
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
                     'Arrival Delay in Minutes': 'arrival_delay',
                     'satisfaction': 'satisfaction'}

        #formato lista para poder pasarlas como parámetro names
        name_cols = list(name_cols.values())

        #creación del dataframe
        df = pd.read_csv('airline_passenger_satisfaction.csv', 
                         header = 0, names = name_cols)
        return df
    
    except FileNotFoundError:
        print(f"El archivo no se encontró.")
        return None
    
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {str(e)}")
        return None


def separate_train_set(df: pd.DataFrame, test_size):
    '''
    Antes de ampliar el EDA, esta función separa el dataframe en test y train.
    A partir de aquí, se trabaja con df_train y se guarda df_test para validación.
    '''
    #separación usando scikit learn train_test_split
    df_to_train, df_test = train_test_split(df, test_size = test_size, random_state = 42)

    #creamos una copia de train
    df_train = df_to_train.copy()
    
    #se guarda el test en un csv para más adelante
    df_test.to_csv('test.csv')

    return df_train


def X_y_separation(df, string_y):
    '''
    Recibe el dataframe completo y el nombre (string) de la columna
    con la variable de salida.
    La función devuelve una matriz X y un vector y separados.
    '''
    #la función drop copia el dataset y elimina la variable de salida
    X = df.drop(string_y, axis = 1)
    
    #copia sólo el vector de salida
    y = df[string_y].copy()
    return X, y