from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from api.routes.patient_routes import PatientRoutes


app = FastAPI(
    title="PredictQ AI Backend",
    description="AI-powered hospital queue management backend",
    version="1.0.0"
)


patient_routes = PatientRoutes()


# =====================================================
# SCHEMAS
# =====================================================

class PatientCreateSchema(BaseModel):
    patient_id: str
    name: str
    department: str
    priority: int


class PatientStatusUpdateSchema(BaseModel):
    status: str


# =====================================================
# ROOT ENDPOINT
# =====================================================

@app.get("/")
def root():
    return {
        "message": "PredictQ AI Backend is running",
        "status": "ACTIVE",
        "version": "1.0.0"
    }


# =====================================================
# HEALTH CHECK
# =====================================================

@app.get("/health")
def health_check():
    return {
        "status": "HEALTHY",
        "service": "PredictQ AI Engine"
    }


# =====================================================
# REGISTER PATIENT
# =====================================================

@app.post("/patients/register")
def register_patient(patient: PatientCreateSchema):

    response = patient_routes.register_patient(
        patient.model_dump()
    )

    if response.get("registered") is False:
        raise HTTPException(
            status_code=400,
            detail=response.get("error")
        )

    return response


# =====================================================
# GET PATIENT
# =====================================================

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):

    response = patient_routes.get_patient(
        patient_id
    )

    if response.get("found") is False:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return response


# =====================================================
# UPDATE PATIENT STATUS
# =====================================================

@app.put("/patients/{patient_id}/status")
def update_patient_status(
    patient_id: str,
    payload: PatientStatusUpdateSchema
):

    response = patient_routes.update_patient_status(
        patient_id,
        payload.status
    )

    if response.get("updated") is False:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return response


# =====================================================
# DELETE PATIENT
# =====================================================

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: str):

    response = patient_routes.delete_patient(
        patient_id
    )

    if response.get("deleted") is False:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return response


# =====================================================
# GET DEPARTMENT PATIENTS
# =====================================================

@app.get("/departments/{department}/patients")
def get_department_patients(department: str):

    return patient_routes.get_department_patients(
        department
    )