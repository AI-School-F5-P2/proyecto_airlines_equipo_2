from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class ModelDataClients(Base):

    __tablename__ = "clients_satisfaction"

    unnamed = Column(Integer)
    id = Column(Integer, primary_key = True)
    gender = Column(String(6))
    customer_type = Column(String(50))
    age = Column(Integer)
    type_travel = Column(String(50))
    clase = Column(String(50))
    flight_distance = Column(Integer)
    wifi_service = Column(Integer)
    departure_arrival_time = Column(Integer)
    online_booking = Column(Integer)
    gate_location = Column(Integer)
    food_drink = Column(Integer)
    online_boarding = Column(Integer)
    seat_comfort = Column(Integer)
    entertain = Column(Integer)
    onboard_service = Column(Integer)
    leg_service = Column(Integer)
    bag_handle = Column(Integer)
    checkin_service = Column(Integer)
    inflight_service = Column(Integer)
    cleanliness = Column(Integer)
    departure_delay = Column(Integer)
    arrival_delay = Column(Float)
    satisfaction = Column(String(50))

    def __str__(self):
        # Define la representación de cadena personalizada para tu objeto
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}"