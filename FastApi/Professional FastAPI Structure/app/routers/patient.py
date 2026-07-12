from fastapi import APIRouter
from app.database import load_data

from fastapi.responses import JSONResponse

from app.models.patient import Patient, PatientUpdate
from app.services.patient_service import (
    create_patient,
    update_patient,
    delete_patient
)

router = APIRouter(prefix="/patients" , tags=["patients"])

@router.get("/view")
def home():
    data = load_data()

    return data


@router.post("/create")
def create(patient: Patient):

    create_patient(patient)

    return JSONResponse(
        status_code=201,
        content={
            "message": "Patient created successfully"
        },
    )


@router.put("/update/{patient_id}")
def update(patient_id: str, patient_update: PatientUpdate):

    update_patient(patient_id, patient_update)

    return {
        "message": "Patient Updated"
    }


@router.delete("/delete/{patient_id}")
def delete(patient_id: str):

    delete_patient(patient_id)

    return {
        "message": "Patient Deleted"
    }