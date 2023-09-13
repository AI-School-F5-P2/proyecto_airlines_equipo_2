import pandas as pd
import pickle
import streamlit as st
import uuid
from PIL import Image

from models_metrics.eval_model import load_data_to_predict

from config.models import ModelDataClients
from config.database import Session

class SatisfactionPredictionApp:
    '''
    Creación de la app con Streamlit. Para visualizar usar el comando: streamlit run main.py
    '''
    def __init__(self):
        with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/pipeline.pkl', 'rb') as archivo:
            self.pipeline = pickle.load(archivo)
        
        with open('C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/catboost_airplanes.pkl', 'rb') as archivo:
            self.model = pickle.load(archivo)
        
        self.logo_path = 'C:/Users/Ana Milena GOMEZ/Documents/Ana Milena GOMEZ/IA-School_Factoria-F5/F5Airlines/proyecto_airlines_equipo_2/images/airline_logo2.png'


    def run(self):
        st.set_page_config(page_title = 'App Predicción de Satisfacción del Cliente',
                           layout = 'centered',
                           initial_sidebar_state = 'auto')

        st.title('Predicción de Satisfacción de los Clientes en la Aerolínea')
        st.markdown('Esta aplicación predice si un usuario está o no está satisfecho con el servicio de la aerolínea.')
        
        with Image.open(self.logo_path) as img:
            st.sidebar.image(img, width = 260)

        st.sidebar.header('Datos ingresados por el usuario:')

        uploaded_file = st.sidebar.file_uploader('Cargue aquí su archivo csv:', type = ['csv'])

        # Valido si el usuario está usando un archivo CSV o introdujo manualmente los datos.
        if uploaded_file is not None:
            input_df = load_data_to_predict(uploaded_file)
        else:
            input_df = self.user_input()

        st.subheader('Datos ingresados por el usuario:')

        if uploaded_file is not None:
            st.write(input_df)
        else:
            st.write('Puede cargar un archivo .csv con la información del usuario o ingresar manualmente los datos en la barra lateral.')
            st.write(input_df)

        X_transformed = self.pipeline.transform(input_df)
        
        prediction, prediction_proba = self.prediction(X_transformed)

        #columnas de predicción y probabilidad
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Predicción')
            st.write(prediction)
             #cambio de color el texto de Prediccion
        
        with col2:
            st.subheader('Probabilidad de Predicción')
            st.write(prediction_proba)
            #cambio de color el grafico de barras
            if prediction_proba[0][1] > 0.50:
                colorPositivo = '#0070B8'
            else:
                colorPositivo = '#ff432d'
            # st.bar_chart(prediction_proba, color = ['#DCDCDC', colorPositivo])

        if prediction == 'neutral or dissatisfied':
            st.markdown('<h1 style="color:#ff432d">El cliente está: Insatisfecho</h1>', unsafe_allow_html = True)
        else:
            st.markdown('<h1 style="color:#228b22">El cliente está: Satisfecho</h1>', unsafe_allow_html = True)

        if st.button('Guardar'):
            self.add_to_database(input_df, prediction[0])


    def prediction(self, X_transformed):
        prediction = self.model.predict(X_transformed)
        prediction_proba = self.model.predict_proba(X_transformed)
        return prediction, prediction_proba


    def generate_unique_key(widget_name):
        return f"{widget_name}_{uuid.uuid4()}"


    def user_input(self):
        #metemos los widgets dentro de un formulario
        with st.sidebar.form(key = 'form1', clear_on_submit = True):

            gender = st.radio("Gender", ['Female', 'Male'])
            
            customer_type = st.radio("Customer Type" , ['Loyal Customer', 'disloyal Customer'])
            
            type_travel = st.radio("Type of Travel", ['Personal Travel', 'Business travel'])
            
            clase = st.radio("Class", ['Eco', 'Eco Plus', 'Business'])
        
            age = st.slider("Age", 0, 99, 25)
            
            flight_distance = st.slider("Flight Distance", 0, 9999, 150) # van de 0 9999 y por defecto en 150
            
            wifi_service = st.slider("Inflight wifi service", 0, 5, 1)
            
            departure_arrival_time = st.slider("Departure/Arrival time", 0, 5, 1)
            
            online_booking = st.slider("Ease of Online booking", 0, 5, 1)
            
            gate_location = st.slider("Gate location", 0, 5, 1)
            
            food_drink = st.slider("Food and drink", 0, 5, 1)
            
            online_boarding = st.slider("Online boarding", 0, 5, 1)
            
            seat_comfort = st.slider("Seat comfort", 0, 5, 1)
            
            entertain = st.slider("Inflight entertainment", 0, 5, 1)
            
            onboard_service = st.slider("On-board service", 0, 5, 1)
            
            leg_service = st.slider("Leg room service", 0, 5, 1)
            
            bag_handle = st.slider("Baggage handling", 0, 5, 1)
            
            checkin_service = st.slider("Checkin service", 0, 5, 1)
            
            inflight_service = st.slider("Inflight service", 0, 5, 1)
            
            cleanliness = st.slider("Cleanliness", 0, 5, 1)
            
            departure_delay = st.slider("Departure Delay in Minutes", 0, 9999, 0)
            
            arrival_delay = st.slider("Arrival Delay in Minutes", 0, 9999, 0)

            boton = st.form_submit_button(label = 'Enviar')

            if boton:
                st.success('Formulario Enviado')

            data_dic = {'unnamed': 0,
                        'id': 0,
                        'gender': gender,
                        'customer_type': customer_type,
                        'age': age,
                        'type_travel': type_travel,
                        'clase': clase,
                        'flight_distance': flight_distance,
                        'wifi_service': wifi_service,
                        'departure_arrival_time': departure_arrival_time,
                        'online_booking': online_booking,
                        'gate_location': gate_location,
                        'food_drink': food_drink,
                        'online_boarding': online_boarding,
                        'seat_comfort': seat_comfort,
                        'entertain': entertain,
                        'onboard_service': onboard_service,
                        'leg_service': leg_service,
                        'bag_handle': bag_handle,
                        'checkin_service': checkin_service,
                        'inflight_service': inflight_service,
                        'cleanliness': cleanliness,
                        'departure_delay': departure_delay,
                        'arrival_delay': arrival_delay}
            
            index = [0]
            
            df = pd.DataFrame(data_dic, index = index)
        
            return df


    def add_to_database(self, input_df, satisfaction):
        '''
        Esta función guarda la información ingresada 
        en una base de datos SQL junto con la predicción.
        '''
        #agregamos el orient para que no se almacene el 0, ('Age': {0: 25})
        input_df_dict = input_df.to_dict(orient = 'records')

        #anexamos la predicción de los datos ingresados por el usuario
        for record in input_df_dict:
            record['satisfaction'] = satisfaction

        try:
            #creamos una sesión de SQLAlchemy
            db = Session()

            #insertamos los registros en la base de datos
            for record in input_df_dict:
                new_data = ModelDataClients(**record)
                db.add(new_data)

            #confirmamos la acción realizada en la base de datos
            db.commit()
            print('Datos almacenados correctamente')
            st.title('¡Datos almacenados correctamente en la base de datos!')
        
        except Exception as e:
            print(f'Error al almacenar datos en la base de datos: {str(e)}')
        
        finally:
            db.close()
