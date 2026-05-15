from ai_engine.database.patient_repository import (
    PatientRepository
)

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class PatientService:

    def __init__(self):

        self.repository = (
            PatientRepository()
        )

    # =====================================================
    # REGISTER PATIENT
    # =====================================================

    def register_patient(
        self,
        patient_data: dict
    ):

        required_fields = [
            "patient_id",
            "name",
            "department",
            "priority"
        ]

        for field in required_fields:

            if field not in patient_data:

                return {
                    "registered": False,
                    "error":
                    f"{field} missing"
                }

        patient_data[
            "status"
        ] = "WAITING"

        result = (
            self.repository.add_patient(
                patient_data
            )
        )

        logger.info(
            f"Patient registered: {patient_data['patient_id']}"
        )

        return {
            "registered": True,
            "patient": result["patient"]
        }

    # =====================================================
    # GET PATIENT
    # =====================================================

    def get_patient(
        self,
        patient_id
    ):

        patient = (
            self.repository.get_patient_by_id(
                patient_id
            )
        )

        if patient is None:

            return {
                "found": False
            }

        return {
            "found": True,
            "patient": patient
        }

    # =====================================================
    # UPDATE STATUS
    # =====================================================

    def update_patient_status(
        self,
        patient_id,
        status
    ):

        patient = (
            self.repository.update_patient_status(
                patient_id,
                status
            )
        )

        if patient is None:

            return {
                "updated": False
            }

        return {
            "updated": True,
            "patient": patient
        }

    # =====================================================
    # DELETE PATIENT
    # =====================================================

    def delete_patient(
        self,
        patient_id
    ):

        deleted = (
            self.repository.delete_patient(
                patient_id
            )
        )

        return {
            "deleted": deleted
        }

    # =====================================================
    # GET DEPARTMENT PATIENTS
    # =====================================================

    def get_department_patients(
        self,
        department
    ):

        patients = (
            self.repository.get_patients_by_department(
                department
            )
        )

        return {
            "count": len(patients),
            "patients": patients
        }