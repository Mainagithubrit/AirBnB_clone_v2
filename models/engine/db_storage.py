#!/usr/bin/python3
"""An sqlalchemy engine"""
from models.base_model import Base
from os import getenv, getenvb
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from sqlalchemy.orm import Session, session, sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base


class DBStorage:
    """Defines a class that creates a database"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_HOST")
        host = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of __object"""
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for e in query:
                key = '{}.{}'.format(type(e).__name__, e.id)
                dic[key] = e
        else:
            list_a = [State, City, User, Place, Review, Amenity]
            for c in list_a:
                query = self.__session.query(c)
                for e in query:
                    key = "{}.{}".format(type(e).__name__, e.id)
                    dic[key] = e
        return (dic)

    def new(self, obj):
        """adds the object to the current database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        and
        create the current database session"""

        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """this function calls remove()"""
        self.__session.close()
