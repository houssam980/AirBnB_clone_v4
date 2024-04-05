#!/usr/bin/python3
'''
    Define class Db_Storage (updated module)
'''
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.state import State
from models.city import City
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        db_dict = {}

        if cls is not None and cls != '':
            objs = self.__session.query(models.classes[cls]).all()
            for obje in objs:
                key = "{}.{}".format(obje.__class__.__name__, obje.id)
                db_dict[key] = obj
            return db_dict
        else:
            for ke, v in models.classes.items():
                if ke != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            db_dict[key] = obj
            return db_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        self.__session.close()

    def get(self, cls, id):
        obj_dict = models.storage.all(cls)
        for ke, v in obj_dict.items():
            matchstring = cls + '.' + id
            if ke == matchstring:
                return v

        return None

    def count(self, cls=None):
        obj_dict = models.storage.all(cls)
        return len(obj_dict)
