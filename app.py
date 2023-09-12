import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from dataBase.api import MySQLAPI
from dataBase.columns_order import Columns_order_class

class SatisfactionPredictionApp:
    def __init__(self):
        self.api = MySQLAPI()
        self.load_clf = pickle.load(open('catboost_airplanes.pkl', 'rb'))
        self.logo = 'images/airline_logo2.png'
        self.column_order = Columns_order_class().columns_order()

    def run(self):
        st.set_page_config(page_title='App pprediccion de satisfaccion del cliente',
                           page_icon=self.logo,
                           layout='centered',
                           initial_sidebar_state='auto'
                           )

        st.title('App de prediccion de satisfaccion de los clientes en la aerolinea')
        st.markdown('Esta aplicacion predice si un usuario esta o no esta satisfecho con el servico de la arolinea')
        # st.sidebar.image(self.logo, width=150)
        st.sidebar.header('Datos ingresados por el usuario')

        uploaded_file = st.sidebar.file_uploader('Cargue aqui su archivo csv', type=['csv'])

        # Valido si el usuario esta usando un archivo CSV o introdujo manualmente los datos.
        if uploaded_file is not None:
            input_df = pd.read_csv(uploaded_file)
        else:
            input_df = self.user_input()

        st.subheader('datos ingresados por el usuario')

        if uploaded_file is not None:
            st.write(input_df)
        else:
            st.write('A la espera de que se cargue el archivo csv, Actualmente usando parametros de entrada de ejemplo (que se muestra a continuacion)')
            st.write(input_df)

        prediction, prediction_proba = self.predict(input_df)

        #Colimnas de prediccion y probabilidad
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Prediccion')
            st.write(prediction)
             #cambio de color el texto de Prediccion
            if prediction == 0:
                st.markdown('<h1 style="color:#ff432d">Insatisfecho</h1>', unsafe_allow_html=True)
            else:
                st.markdown('<h1 style="color:#0070B8">Satisfecho</h1>', unsafe_allow_html=True)

        with col2:
            st.subheader('Probabilidad de Prediccion')
            st.write(prediction_proba)
            #cambio de color el grafico de barras
            if prediction_proba[0][1] > 0.50:
                colorPositivo = '#0070B8'
            else:
                colorPositivo = '#ff432d'
            st.bar_chart(
                prediction_proba,
                color=['#DCDCDC', colorPositivo]
            )

        if st.button('Guardar'):
            self.add_to_database(input_df, prediction[0])

        st.write('')
        st.write('')
        st.write('')
        
        # Tabla de datos pasados obtenidos.
        st.title('Datos almacenados')
        data = self.api.obtener_datos()
        df = pd.DataFrame(data)
        st.write(df)

    def user_input(self):
        #Creo los witgets
        st.sidebar.markdown("""Genero""")
        male = st.sidebar.checkbox("Gender_Male:", value=False)
        female = st.sidebar.checkbox("Gender_Female:", value=False)
        st.sidebar.markdown("""Tipo de cliente""")
        loyal_customer = st.sidebar.checkbox("Customer Type_Loyal Customer", value=False)
        disloyal_customer = st.sidebar.checkbox("Customer Type_disloyal Customer", value=False)
        st.sidebar.markdown("""Tipo de viaje""")
        travel_business = st.sidebar.checkbox("Type of Travel_Business travel", value=False)
        travel_personal = st.sidebar.checkbox("Type of Travel_Personal Travel", value=False)
        st.sidebar.markdown("""Clase""")
        class_bussines = st.sidebar.checkbox("Class_Business", value=False)
        class_eco = st.sidebar.checkbox("Class_Eco", value=False)
        class_eco_plus = st.sidebar.checkbox("Class_Eco Plus", value=False)
        st.sidebar.markdown("""...""")
        age = st.sidebar.slider("age", 0, 99, 25)
        flight_distance = st.sidebar.slider("flight_distance", 0, 9999, 150) # van de 0 9999 y por defecto en 150
        inflight_wifi_services = st.sidebar.slider("inflight_wifi_services", 0, 5, 1)
        departure_arrival_time = st.sidebar.slider("departure_arrival_time ", 0, 5, 1)
        ease_of_online_booking = st.sidebar.slider("ease_of_online_booking ", 0, 5, 1)
        gate_location = st.sidebar.slider("gate_location", 0, 5, 1)
        foot_and_drink = st.sidebar.slider("foot_and_drink", 0, 5, 1)
        online_boarding = st.sidebar.slider("online_boarding", 0, 5, 1)
        seat_confort = st.sidebar.slider("seat_confort ", 0, 5, 1)
        inflight__entertainment = st.sidebar.slider("inflight__entertainment", 0, 5, 1)
        on_boart_services = st.sidebar.slider("on_boart_services ", 0, 5, 1)
        leg_room__services = st.sidebar.slider("leg_room__services", 0, 5, 1)
        baggage_handing = st.sidebar.slider("baggage_handing", 0, 5, 1)
        cheking_services = st.sidebar.slider("cheking_services", 0, 5, 1)
        inflight_services = st.sidebar.slider("inflight_services", 0, 5, 1)
        cleanlines = st.sidebar.slider("cleanlines", 0, 5, 1)
        departure_delay_in_minutes = st.sidebar.slider("departure_delay_in_minutes", 0, 9999, 0)
        arrival_delay_in_minutes = st.sidebar.slider("arrival_delay_in_minutes", 0, 9999, 0)
        
        data_dict = {
            'Flight Distance':flight_distance,
            'Inflight wifi service': inflight_wifi_services,
            'Age':age,
            'Departure/Arrival time convenient': departure_arrival_time,  
            'Ease of Online booking': ease_of_online_booking,
            'Gate location': gate_location,
            'Food and drink': foot_and_drink,
            'Online boarding': online_boarding,
            'Seat comfort': seat_confort,
            'Inflight entertainment': inflight__entertainment,
            'On-board service': on_boart_services,
            'Leg room service': leg_room__services,
            'Baggage handling': baggage_handing,
            'Checkin service': cheking_services,
            'Inflight service': inflight_services,
            'Cleanliness': cleanlines,
            'Departure Delay in Minutes': departure_delay_in_minutes,
            'Arrival Delay in Minutes': arrival_delay_in_minutes,
            'Gender_Female':female,
            'Gender_Male':male,
            'Customer Type_Loyal Customer': loyal_customer,
            'Customer Type_disloyal Customer':disloyal_customer,
            'Type of Travel_Business travel':travel_business,
            'Type of Travel_Personal Travel':travel_personal,
            'Class_Business':class_bussines,
            'Class_Eco':class_eco,
            'Class_Eco Plus':class_eco_plus,  
        }
        
        # Ordenos los nombres de las columnas en el mismo orden del dataset con el que se entreno al modelo
        # para que no haya errores al momento de hacer la prediccion
        data = {key: data_dict[key] for key in self.column_order}
        features = pd.DataFrame(data, index=[0])
        return features

    def predict(self, input_df):
        prediction = self.load_clf.predict(input_df)
        prediction_proba = self.load_clf.predict_proba(input_df)
        return prediction, prediction_proba

    def add_to_database(self, input_df, satisfaction):
        #agrego el orente para que no se almacene el 0, ('Age': {0: 25})
        input_df_list = input_df.to_dict(orient='records') 
        #Creo un Nuevo valor
        nuevo_valor = {'satisfaction': satisfaction}
        #edito el último elemento de la lista
        input_df_list[-1].update(nuevo_valor)
        # envio la lista de diccionarios actualizada
        self.api.agregar_cliente(input_df_list)

if __name__ == "__main__":
    app = SatisfactionPredictionApp()
    app.run()
