from fastapi import FastAPI
from typing import Union
import schemas
import services
app = FastAPI()

@app.get('/emailingapi/get/users/all')
def getusers():
    services.getallusers()
    
@app.post('/emalingapi/post/users')
def makeusers(user_data:schemas.User):
    return services.adduser(user_data)


@app.post('emailingapi/post/sendemail/users')
def sendemailtoall(email_data:schemas.EmailData):
    return services.sendmail(email_data)
    