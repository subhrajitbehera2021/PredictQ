from ai_engine.services.patient_service import (
    PatientService
)


class PatientRoutes:

    def __init__(self):

        self.patient_service = PatientService()

    def register_patient(
        self,
        request_data: dict
    ):

        return self.patient_service.register_patient(
            request_data
        )

    def get_patient(
        self,
        patient_id
    ):

        return self.patient_service.get_patient(
            patient_id
        )

    def update_patient_status(
        self,
        patient_id,
        status: str
    ):

        return self.patient_service.update_patient_status(
            patient_id,
            status
        )

    def delete_patient(
        self,
        patient_id
    ):

        return self.patient_service.delete_patient(
            patient_id
        )

    def get_department_patients(
        self,
        department: str
    ):

        return self.patient_service.get_department_patients(
            department
        )