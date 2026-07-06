
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : Annotated[str,Field(max_length=50,title='Name of the patient',description='give the name of the patient in less then 50 chars',examples='jakaria hossain')]
    email:EmailStr # this ues for email valid verifide
    linkedin_url:AnyUrl # this usr for any link valid verifide
    age : int
    weight: Annotated[float,Field(gt=0,strict=True)] # this usr for condison
    married: Annotated[bool,Field(default=False,description='is the patient married or not')]
    allergies: List[str] = Field(max_length=5)
    contact_details: Dict[str,str]


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

patient_info = {'name':'jakaria','age':33,'weight':32.3,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'1111111'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)