import streamlit as st

class Sidebar:
    def __init__(self):
        return
    
    
    def sidebar(self):
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