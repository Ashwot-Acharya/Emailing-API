from fastapi import FastAPI
from typing import Union
import schemas
import services
app = FastAPI()

@app.get('/emailingapi/get/users/all')
def getusers():
    # do admin auth
    services.getallusers()
    
@app.post('/emalingapi/post/users')
def makeusers(user_data:schemas.user):
    # make users
    return services.adduser(user_data)


@app.post('emailingapi/post/sendemail/users')
def sendemailtoall():
    pass    
    
    