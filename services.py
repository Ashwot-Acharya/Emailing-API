import schemas 
import models as _models
import connect 
import sqlalchemy.orm as orm
import fastapi as _fastapi 


def get_db():
    db =  connect.Sessionlocal()
    try: 
        return db
    finally:
        db.close()


def adduser(user_data:schemas.user ,db:orm.Session = get_db()):
    try:
        db.add(user_data)
        db.commit()
        db.refresh(user_data)
        return {"success":f" User added {user_data.name}"}
    except Exception as e:
        raise _fastapi.HTTPException(422, "Error has occured")


def getallusers():
    pass    


def removeuser(name , email):
    pass


def sendEmail(email):
    # we need to get emails and send to this function one by one and then send email
    pass
