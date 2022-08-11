#!/usr/bin/python3
"""Adding a storage engine with SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = [User, Place, State, City, Amenity, Review]


class DBStorage():
    """New engine DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Public instance methods that an engine creates"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True))

    if getenv('HBNB_ENV') == 'test':
        Base.metadata.drop_all()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        new_dict = {}

        if cls in classes:
            obj = self.__session.query(cls).all()

            for row in obj:
                key = type(row).__name__ + "." + row.id
                new_dict[key] = row

        else:
            for clase in classes:
                obj = self.__session.query(clase).all()

                for row in obj:
                    key = type(row).__name__ + "." + row.id
                    new_dict[key] = row

        return new_dict

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """remove the current session from the obj database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (SQLAlchemy function)"""
        Base.metadata.create_all(self.__engine)

        """""create the current database session"""
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)

        self.__session = Session()
