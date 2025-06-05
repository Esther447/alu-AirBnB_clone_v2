#!/usr/bin/python3
from models import storage
from models.city import City

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns list of City instances with state_id == State.id"""
            return [city for city in storage.all(City).values() if city.state_id == self.id]
