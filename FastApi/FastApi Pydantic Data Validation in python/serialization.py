
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

temp = patient1.model_dump(exclude=['name','age']) # include =['name','age'] this only show name and age and exclude=['name','age'] this is show without name and age  and other exclude_unset = True
print(patient1.name)
print(temp)

   

