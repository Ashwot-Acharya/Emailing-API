import schemas 
from fastapi import Depends , HTTPException
import models
import connect 
import os
from sqlalchemy.orm import Session


def get_db():
    db =  connect.Sessionlocal()
    try: 
        return db
    finally:
        db.close()


def adduser(user_data , db:Session = get_db()):
   
        db_user = models.User(name = user_data.name , email = user_data.email)
        db.add(db_user)
        db.commit()
        return {"success":f" User added {user_data.name}"}

        
def sendemail(email_data):
    pass


def getallusers(db:Session = get_db()):
    allusrs = db.query(models.User).all()
    return allusrs

def getusers(user_id:int , db:Session= get_db()):
    user = db.query( models.User).filter(models.User.id == user_id).first()
    return user

def CreateAdmin(admindata ,  password):
    if ( password =  os. )

        