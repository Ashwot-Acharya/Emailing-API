from pydantic import BaseModel


class User(BaseModel):
    name :str 
    email :str 
    class config:
        orm_mode = True

class EmailData(BaseModel):
    title : str
    body : str
    class config:
        orm_mode = True