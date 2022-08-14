from pydantic import BaseModel


class user(BaseModel):
    name :str 
    email :str 
    class config:
        orm_mode = True