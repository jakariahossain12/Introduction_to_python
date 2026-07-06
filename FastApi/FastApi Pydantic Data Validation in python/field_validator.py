
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr 
    linkedin_url:AnyUrl 
    age : int
    weight: float
    married: Annotated[bool,Field(default=False,description='is the patient married or not')]
    allergies: List[str] = Field(max_length=5)
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age', mode='after') #this is the mode default value after and before typer conversion
    @classmethod
    def validate_age(cls, value):
        if 0 < value <100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

patient_info = {'name':'jakaria','age':33,'weight':32.3,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'1111111'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)