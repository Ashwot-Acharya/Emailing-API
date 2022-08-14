import connect 
from sqlalchemy import create_engine
from sqlalchemy import Column , String , DateTime, Integer
from datetime import datetime
import os 

class user(connect.Base):
    __tablename__ = "users"
    id = Column(Integer() , primary_key = True)
    name = Column(String(50), nullable = False, )
    email = Column(String(150), unique = True , nullable =False)
    date_create = Column(DateTime() , default = datetime.utcnow)
   

