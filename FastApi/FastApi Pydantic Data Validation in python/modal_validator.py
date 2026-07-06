
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
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

    @model_validator(mode='after') # mode hsa two value after and before
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older then 60 must have an emergency contact')
        return model


   


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

patient_info = {'name':'jakaria','age':33,'weight':32.3,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'1111111'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)