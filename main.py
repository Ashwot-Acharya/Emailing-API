from fastapi import FastAPI
from typing import Union
import schemas
import services
app = FastAPI()

@app.get('/')
def getusers():
    return services.getallusers()
    
@app.post('/post/user')
def createuser(user_data: schemas.User):
    return services.adduser(user_data)
