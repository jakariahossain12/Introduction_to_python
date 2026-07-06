
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated


class Address(BaseModel):
    city:str
    state: str
    pin:str

class Patient(BaseModel):
    name:str
    email:str  
    age : int
    address: Address
    


address_dict ={'city':'dhaka','state':'savar','pin':'3333'}

address1 = Address(**address_dict)

patient_dict = {'name':'jakaria','email':'kajaria@gmail.com','age':33,'address':address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.pin)
 

   

