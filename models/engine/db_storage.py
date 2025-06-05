#!/usr/bin/python3
"""This module defines the DBStorage class for MySQL storage using SQLAlchemy"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import pymysql
pymysql.install_as_MySQLdb()


from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
    __session = None

    def __init__(self):
        # session setup (inside reload)
        pass

    def reload(self):
        from models.base_model import Base
        from models import classes
        engine = create_engine(self.__engine_url, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Closes the current SQLAlchemy session."""
        if self.__session:
            self.__session.remove()
