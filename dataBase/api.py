import mysql.connector
import numpy as np
from decouple import config
from dataBase.columns_order import Columns_order_class

class MySQLAPI:
    def __init__(self):
        # Configura la conexión a la base de datos MySQL
        self.db = mysql.connector.connect(
         
            host= config('HOST'),
            user = config('USER'),
            password = config('PASSWOR'),
            database= config('DATABASE'),
        )
        
        self.columns_order = Columns_order_class().columns_order()
    
    def agregar_cliente(self, data):
        # Crear una lista con los nombres de las columnas en el orden correcto
        self.columns_order += ['satisfaction'] #agrego un nuevo valor al array
        
        # Crear una lista de valores ordenados de acuerdo a column_order
        values = [data[0][col] for col in self.columns_order]
        
        # Convertir valores de tipo numpy.int64 a int
        values = [int(val) if isinstance(val, np.int64) else val for val in values]
        
        # Definir la consulta SQL con marcadores de posición
        sql_insert = """
            INSERT INTO passenger_airlines (
                Age, `Flight Distance`, `Inflight wifi service`, `Departure/Arrival time convenient`,
                `Ease of Online booking`, `Gate location`, `Food and drink`, `Online boarding`, `Seat comfort`,
                `Inflight entertainment`, `On-board service`, `Leg room service`, `Baggage handling`, `Checkin service`,
                `Inflight service`, `Cleanliness`, `Departure Delay in Minutes`, `Arrival Delay in Minutes`,
                `Gender_Female`, `Gender_Male`, `Customer Type_Loyal Customer`, `Customer Type_disloyal Customer`,
                `Type of Travel_Business travel`, `Type of Travel_Personal Travel`, `Class_Business`, `Class_Eco`,
                `Class_Eco Plus`, `satisfaction`
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """
        
        # Ejecutar la consulta SQL
        cursor = self.db.cursor()
        cursor.execute(sql_insert, tuple(values))
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
    
    
    
    
    
    
    