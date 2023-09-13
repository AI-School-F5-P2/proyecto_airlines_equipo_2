from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

database = config('DATABASE')
password = config('PASSWORD')
user = config('USER')
localhost = config('LOCALHOST')

router = f"mysql+pymysql://{user}:{password}@{localhost}:3306/{database}"

#creamos la conexión a la base de datos
engine = create_engine(router)

meta_data = MetaData()

#los cambios en la base de datos deben hacerse manualmente pues autocommit = False
Session = sessionmaker(autocommit = False, bind = engine)

#creamos una instancia de declarative_base() para que los Modelos/Tablas puedan heredar de esta clase
Base = declarative_base()