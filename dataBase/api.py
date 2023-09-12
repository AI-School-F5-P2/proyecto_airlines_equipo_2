import mysql.connector
import numpy as np
from decouple import config
from config.models import ModelDataClients
from dataBase.columns_order import Columns_order_class
from config.database import Session

class MySQLAPI:
    def __init__(self):
        self.db_session = Session()

    def agregar_cliente(self, data):
        try:
            # Insertamos los registros en la base de datos
            new_data = ModelDataClients(**data)
            self.db_session.add(new_data)
            # Confirmamos la acción realizada en la base de datos
            self.db_session.commit()
            return 'ok'
        except Exception as e:
            print(f'Error al almacenar datos en la base de datos: {str(e)}')
        finally:
            self.db_session.close()




    def obtener_datos(self):
        try:
            # Realizo una consulta para obtener todos los clientes
            datos = self.db_session.query(ModelDataClients).all()

            # Convierto los objetos ModelDataClients en diccionarios
            datos_json = [cliente.__dict__ for cliente in datos]
            
            # Elimino la clave '_sa_instance_state' de cada diccionario
            for cliente_json in datos_json:
                cliente_json.pop('_sa_instance_state', None)
            
            return datos_json
        except Exception as e:
            print(f'Error al obtener datos de la base de datos: {str(e)}')
        finally:
            self.db_session.close()


if __name__ == '__main__':
    api = MySQLAPI()
    api.obtener_datos()

    
    