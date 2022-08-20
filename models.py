import connect 
from sqlalchemy import create_engine
from sqlalchemy import Column , String , DateTime, Integer
from datetime import datetime
import os 

Base = connect.Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer() , primary_key = True , index = True)
    name = Column(String(50), nullable = False, index = True )
    email = Column(String(150), unique = True , nullable =False)
    date_create = Column(DateTime() , default = datetime.utcnow)
   

