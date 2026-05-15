from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class PatientRepository:

    def __init__(self):

        self.patients = []

    def add_patient(
        self,
        patient_data: dict
    ):

        self.patients.append(patient_data)

        logger.info(
            f"Patient added: {patient_data.get('patient_id')}"
        )

        return {
            "saved": True,
            "patient": patient_data
        }

    def get_all_patients(self):

        return self.patients

    def get_patient_by_id(
        self,
        patient_id
    ):

        for patient in self.patients:

            if patient.get("patient_id") == patient_id:
                return patient

        return None

    def get_patients_by_department(
        self,
        department: str
    ):

        return [
            patient
            for patient in self.patients
            if patient.get("department") == department
        ]

    def get_patients_by_priority(
        self,
        priority: int
    ):

        return [
            patient
            for patient in self.patients
            if patient.get("priority") == priority
        ]

    def update_patient_status(
        self,
        patient_id,
        status: str
    ):

        patient = self.get_patient_by_id(
            patient_id
        )

        if patient is None:
            return None

        patient["status"] = status

        logger.info(
            f"Patient status updated: {patient_id}"
        )

        return patient

    def delete_patient(
        self,
        patient_id
    ):

        patient = self.get_patient_by_id(
            patient_id
        )

        if patient is None:
            return False

        self.patients.remove(patient)

        logger.info(
            f"Patient deleted: {patient_id}"
        )

        return True