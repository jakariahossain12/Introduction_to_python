from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID", examples=["P001"])]
    name: Annotated[str, Field(...)]
    city: Annotated[str, Field(...)]
    age: Annotated[int, Field(gt=0, lt=120)]
    gender: Annotated[
        Literal["male", "female", "others"],
        Field(...)
    ]
    height: Annotated[float, Field(gt=0)]
    weight: Annotated[float, Field(gt=0)]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Annotated[Optional[int], Field(gt=0)] = None
    gender: Optional[Literal["male", "female", "others"]] = None
    height: Annotated[Optional[float], Field(gt=0)] = None
    weight: Annotated[Optional[float], Field(gt=0)] = None