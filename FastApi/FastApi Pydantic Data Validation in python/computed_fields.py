
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr 
    linkedin_url:AnyUrl 
    age : int
    weight: float
    height: float
    married: Annotated[bool,Field(default=False,description='is the patient married or not')]
    allergies: List[str] = Field(max_length=5)
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

 

   


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

patient_info = {'name':'jakaria','age':33,'weight':32.3,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'1111111'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)