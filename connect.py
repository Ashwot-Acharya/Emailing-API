from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.ext.declarative as declarative
import os 

Base = declarative.declarative_base()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(BASE_DIR,'mydb.db' )

engine = create_engine(connection_string, echo = True)

Sessionlocal = sessionmaker(autocommit=False , autoflush=False , bind = engine)