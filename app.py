import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pickle 
from sklearn.preprocessing import LabelEncoder
from api import MySQLAPI


api = MySQLAPI()
logo = 'airline_logo2.png'

st.set_page_config(page_title= 'App pprediccion de satifaccion del cliente',
                   page_icon=logo,
                   layout='centered',
                   initial_sidebar_state='auto'
                   )

st.title('App de prediccion de satisafaccion de los clientes en la aerolinea')
st.markdown('Esta aplicacion predice si un usuario esta o no esta satisfecho con el servico de la arolinea')
st.sidebar.image(logo, width=150)
st.sidebar.header('Datos ingresados por el usuario')

#Archivo CSV cargado por el usuario
uploaded_file = st.sidebar.file_uploader('Cargue aqui su archivo csv', type=['csv'])

# Datos ingresados manualmente por el usuario
def user_input():
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
        
        #guardo los datos obtenidos en un diccionario
        data = {   
            'Age':age,
            'Flight Distance':flight_distance,
            'Inflight wifi service': inflight_wifi_services,
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
        
        #convertimos el diccionario a un dataframe
        features = pd.DataFrame(data, index=[0])
        # features.to_csv('datos6.csv', index=False) 
        return features


if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    input_df = user_input()



st.subheader('datos ingresados por el usuario')

if uploaded_file is not None:
    st.write(input_df)
else:
    st.write('A la espera de que se cargue el archivo csv, Actualmente usando parametros de entrada de ejemplo (que se muestra a continuacion)')
    st.write(input_df)
    




#cargamos el modelo de claificacion previamente entrenado
load_clf = pickle.load(open('heart2.pkl', 'rb'))

#aplicamos el modelo para realizar predicciones en base a los datosingresados
prediction = load_clf.predict(input_df)
prediction_proba = load_clf.predict_proba(input_df)


col1, col2 = st.columns(2)
with col1:
    st.subheader('Prediccion')
    st.write(prediction)
    #cambio de color el texto
    if prediction == 0:
        st.markdown('<h1 style="color:#ff432d">Insatisfecho</h1>', unsafe_allow_html=True)
    else:
        st.markdown('<h1 style="color:#0070B8">Satisfecho</h1>', unsafe_allow_html=True)
    
    
with col2:
    st.subheader('Probabilidad de Prediccion')
    st.write(prediction_proba)
    #cambio de color de la barra
    if prediction_proba[0][1] > 0.50:
        colorPositivo = '#0070B8'
    else:
        colorPositivo = '#ff432d'
    # Grafico de barra
    st.bar_chart(
        prediction_proba,
        color=['#DCDCDC',colorPositivo]
        )





#Funcion para almacenar en la base de datos
def agregar_BD():
    input_df_list = input_df.to_dict(orient='records')#agrego el orente para que no se almacene el 0, ('Age': {0: 25}) 
    #Creo un Nuevo valor
    nuevo_valor = {'satisfaction': prediction[0]}
    #último diccionario de la lista y agreg0 las claves y valores del nuevo diccionario
    input_df_list[-1].update(nuevo_valor)
    # envio la lista de diccionarios actualizada
    api.agregar_cliente(input_df_list)
    
    

#Boton de guargar los datos
st.button('Guardar',  on_click=agregar_BD())
  

# Tabla de datos pasados obtenidos.
st.title('Datos pasados almacenados')
data = api.obtener_datos()
df = pd.DataFrame(data)
st.write(df)
