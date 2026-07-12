from fastapi import HTTPException

from app.database import load_data,save_data
from app.models.patient import Patient , PatientUpdate

# from app.database import load_data, save_data
# from app.models.patient import Patient


def create_patient(patient : Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient already exists"
        )

    data[patient.id] = patient.model_dump(exclude={"id"})

    save_data(data)


def update_patient(patient_id, patient_update : PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    patient = data[patient_id]

    updates = patient_update.model_dump(exclude_unset=True)

    patient.update(updates)

    patient["id"] = patient_id

    patient = Patient(**patient)

    data[patient_id] = patient.model_dump(exclude={"id"})

    save_data(data)


def delete_patient(patient_id : str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    del data[patient_id]

    save_data(data)