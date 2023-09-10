import pandas as pd
import pickle
import streamlit as st
import uuid
# from dataBase.api import MySQLAPI
# from dataBase.columns_order import Columns_order_class

from models_metrics.eval_model import load_data_to_predict

class SatisfactionPredictionApp:
    def __init__(self):
        # self.api = MySQLAPI()
        self.pipeline = pickle.load(open('pipeline.pkl', 'rb'))
        self.model = pickle.load(open('catboost_airplanes.pkl', 'rb'))
        self.logo = 'images/airline_logo2.png'
        # self.column_order = Columns_order_class().columns_order()

    def run(self):
        st.set_page_config(page_title = 'App Predicción de Satisfacción del Cliente',
                           page_icon = self.logo,
                           layout = 'centered',
                           initial_sidebar_state = 'auto')

        st.title('App de Predicción de Satisfacción de los Clientes en la Aerolínea')
        st.markdown('Esta aplicación predice si un usuario está o no está satisfecho con el servicio de la arolínea')
        # st.sidebar.image(self.logo, width=150)
        st.sidebar.header('Datos ingresados por el usuario')

        uploaded_file = st.sidebar.file_uploader('Cargue aquí su archivo csv', type = ['csv'])

        # Valido si el usuario está usando un archivo CSV o introdujo manualmente los datos.
        if uploaded_file is not None:
            input_df = load_data_to_predict(uploaded_file)
        else:
            input_df = self.user_input()

        st.subheader('Datos ingresados por el usuario')

        if uploaded_file is not None:
            st.write(input_df)
        else:
            st.write('A la espera de que se cargue el archivo csv. Actualmente usando parámetros de entrada de ejemplo (que se muestra a continuación)')
            st.write(input_df)

        X_transformed = self.pipeline.transform(input_df)
        
        prediction, prediction_proba = self.prediction(X_transformed)

        #columnas de predicción y probabilidad
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Predicción')
            st.write(prediction)
             #cambio de color el texto de Prediccion
            if prediction == 'neutral or dissatisfied':
                st.markdown('<h1 style="color:#ff432d">Insatisfecho</h1>', unsafe_allow_html = True)
            else:
                st.markdown('<h1 style="color:#0070B8">Satisfecho</h1>', unsafe_allow_html = True)

        with col2:
            st.subheader('Probabilidad de Predicción')
            st.write(prediction_proba)
            #cambio de color el grafico de barras
            if prediction_proba[0][1] > 0.50:
                colorPositivo = '#0070B8'
            else:
                colorPositivo = '#ff432d'
            st.bar_chart(prediction_proba, color = ['#DCDCDC', colorPositivo])

        if st.button('Guardar'):
            self.add_to_database(input_df, prediction[0])

        st.write('')
        st.write('')
        st.write('')
        
        # Tabla de datos pasados obtenidos.
        st.title('Datos Almacenados')
        data = self.api.obtener_datos()
        df = pd.DataFrame(data)
        st.write(df)

    def prediction(self, X_transformed):
        prediction = self.model.predict(X_transformed)
        prediction_proba = self.model.predict_proba(X_transformed)
        return prediction, prediction_proba
    
    def generate_unique_key(widget_name):
        return f"{widget_name}_{uuid.uuid4()}"

    def user_input(self):
        #creamos los witgets
        st.sidebar.markdown("""Género""")
        gender = st.sidebar.radio("Gender", ['Female', 'Male'])
        
        st.sidebar.markdown("""Tipo de cliente""")
        customer_type = st.sidebar.radio("Customer Type" , ['Loyal Customer', 'disloyal Customer'])
        
        st.sidebar.markdown("""Tipo de viaje""")
        type_travel = st.sidebar.radio("Type of Travel", ['Personal Travel', 'Business travel'])
        
        st.sidebar.markdown("""Clase""")
        clas = st.sidebar.radio("Class", ['Eco', 'Eco Plus', 'Business'])
    
        st.sidebar.markdown("""...""")
        age = st.sidebar.slider("Age", 0, 99, 25)
        
        flight_distance = st.sidebar.slider("Flight Distance", 0, 9999, 150) # van de 0 9999 y por defecto en 150
        
        wifi_service = st.sidebar.slider("Inflight wifi service", 0, 5, 1)
        
        departure_arrival_time = st.sidebar.slider("Departure/Arrival time", 0, 5, 1)
        
        online_booking = st.sidebar.slider("Ease of Online booking", 0, 5, 1)
        
        gate_location = st.sidebar.slider("Gate location", 0, 5, 1)
        
        food_drink = st.sidebar.slider("Food and drink", 0, 5, 1)
        
        online_boarding = st.sidebar.slider("Online boarding", 0, 5, 1)
        
        seat_comfort = st.sidebar.slider("Seat comfort", 0, 5, 1)
        
        entertain = st.sidebar.slider("Inflight entertainment", 0, 5, 1)
        
        onboard_service = st.sidebar.slider("On-board service", 0, 5, 1)
        
        leg_service = st.sidebar.slider("Leg room service", 0, 5, 1)
        
        bag_handle = st.sidebar.slider("Baggage handling", 0, 5, 1)
        
        checkin_service = st.sidebar.slider("Checkin service", 0, 5, 1)
        
        inflight_service = st.sidebar.slider("Inflight service", 0, 5, 1)
        
        cleanliness = st.sidebar.slider("Cleanliness", 0, 5, 1)
        
        departure_delay = st.sidebar.slider("Departure Delay in Minutes", 0, 9999, 0)
        
        arrival_delay = st.sidebar.slider("Arrival Delay in Minutes", 0, 9999, 0)