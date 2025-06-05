#!/usr/bin/python3
"""This module defines the DBStorage class for MySQL storage using SQLAlchemy"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import pymysql
pymysql.install_as_MySQLdb()


class DBStorage:
    """Interacts with the MySQL database via SQLAlchemy ORM"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{passwd}@{host}/{db}',
            pool_pre_ping=True
        )

        if env == "test":
            # Drop all tables if in test environment
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects of the given class.
        If cls is None, query all types of objects.

        Returns:
            dict: Dictionary of objects in the format <class name>.<id> : object
        """
        dic = {}

        classes = [State, City, User, Place, Review, Amenity]

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls).all()
            for obj in query:
                key = f"{obj.__class__.__name__}.{obj.id}"
                dic[key] = obj
        else:
            for cl in classes:
                query = self.__session.query(cl).all()
                for obj in query:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    dic[key] = obj

        return dic

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Remove the current session"""
        self.__session.close()

