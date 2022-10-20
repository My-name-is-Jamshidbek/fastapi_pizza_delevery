from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                "username":"johndoe",
                "email":"johndoe@mail.com",
                "password":"password",
                'is_staff':False,
                'is_active':True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str='f9ac80fc96b3620d70c08e01bc536cf33ca0f6419dbeb8fff8aed1d5ac677489'


class LoginModel(BaseModel):
    username:str
    password:str


class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]


    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }