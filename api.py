import mysql.connector
import numpy as np

class MySQLAPI:
    def __init__(self):
        # Configura la conexión a la base de datos MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="airlines"
        )
    
    def agregar_cliente(self, data):
            # # Obtener los valores de las variables
            Age = data[0]['Age']
            Flight_Distance = data[0]['Flight Distance']
            Inflight_wifi_service = data[0]['Inflight wifi service']
            Departure_Arrival_time_convenient = data[0]['Departure/Arrival time convenient']
            Ease_of_Online_booking = data[0]['Ease of Online booking']
            Gate_location = data[0]['Gate location']
            Food_and_drink = data[0]['Food and drink']
            Online_boarding = data[0]['Online boarding']
            Seat_comfort = data[0]['Seat comfort']
            Inflight_entertainment = data[0]['Inflight entertainment']
            On_board_service = data[0]['On-board service']
            Leg_room_service = data[0]['Leg room service']
            Baggage_handling = data[0]['Baggage handling']
            Checkin_service = data[0]['Checkin service']
            Inflight_service = data[0]['Inflight service']
            Cleanliness = data[0]['Cleanliness']
            Departure_Delay_in_Minutes = data[0]['Departure Delay in Minutes']
            Arrival_Delay_in_Minutes = data[0]['Arrival Delay in Minutes']
            Gender_Female = data[0]['Gender_Female']
            Gender_Male = data[0]['Gender_Male']
            Customer_Type_Loyal_Customer = data[0]['Customer Type_Loyal Customer']
            Customer_Type_disloyal_Customer = data[0]['Customer Type_disloyal Customer']
            Type_of_Travel_Business_travel = data[0]['Type of Travel_Business travel']
            Type_of_Travel_Personal_Travel = data[0]['Type of Travel_Personal Travel']
            Class_Business = data[0]['Class_Business']
            Class_Eco = data[0]['Class_Eco']
            Class_Eco_Plus = data[0]['Class_Eco Plus']
            Satisfaction = data[0]['satisfaction']

            # Crear una tupla con los valores a insertar
            values = (
                Age, Flight_Distance, Inflight_wifi_service, Departure_Arrival_time_convenient, Ease_of_Online_booking,
                Gate_location, Food_and_drink, Online_boarding, Seat_comfort, Inflight_entertainment,
                On_board_service, Leg_room_service, Baggage_handling, Checkin_service, Inflight_service,
                Cleanliness, Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes, Gender_Female, Gender_Male,
                Customer_Type_Loyal_Customer, Customer_Type_disloyal_Customer, Type_of_Travel_Business_travel,
                Type_of_Travel_Personal_Travel, Class_Business, Class_Eco, Class_Eco_Plus, Satisfaction
            )
            
            # Convertir valores de tipo numpy.int64 a int
            values = tuple(int(val) if isinstance(val, np.int64) else val for val in values)
            
            # Defino la consulta SQL con marcadores de posición
            sql_insert = """
                INSERT INTO passenger_airlines (
                     Age, `Flight Distance`, `Inflight wifi service`, `Departure/Arrival time convenient`, `Ease of Online booking`,
                    `Gate location`, `Food and drink`, `Online boarding`, `Seat comfort`, `Inflight entertainment`,
                    `On-board service`, `Leg room service`, `Baggage handling`, `Checkin service`, `Inflight service`,
                    `Cleanliness`, `Departure Delay in Minutes`, `Arrival Delay in Minutes`, `Gender_Female`, `Gender_Male`,
                    `Customer Type_Loyal Customer`, `Customer Type_disloyal Customer`, `Type of Travel_Business travel`,
                    `Type of Travel_Personal Travel`, `Class_Business`, `Class_Eco`, `Class_Eco Plus`, `satisfaction`
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
            """
            
            # Ejecutar la consulta SQL
            cursor = self.db.cursor()
            cursor.execute(sql_insert, values)
            self.db.commit()

            return {"mensaje": "Cliente agregado correctamente"}






    # Ruta para obtener todos los clientes de la base de datos
    def obtener_datos(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM passenger_airlines")  # Reemplaza 'tu_tabla' con el nombre de tu tabla
        datos = cursor.fetchall()
        cursor.close()
        return datos











if __name__ == '__main__':
    api = MySQLAPI()
    api.obtener_datos()
    
    
    
    
    
    
    