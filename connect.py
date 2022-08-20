from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os 

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(BASE_DIR,'mydb.db' )

engine = create_engine(connection_string, connect_args={"check_same_thread": False} ,echo = True)

Sessionlocal = sessionmaker(autocommit=False , autoflush=False , bind = engine)


Base = declarative_base()
