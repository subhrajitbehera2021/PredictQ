from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class DoctorAvailabilityEngine:

    def __init__(self):

        self.doctors = {}

    # =====================================================
    # REGISTER DOCTOR
    # =====================================================

    def register_doctor(
        self,
        doctor_id: str,
        name: str,
        department: str
    ):

        self.doctors[doctor_id] = {
            "doctor_id": doctor_id,
            "name": name,
            "department": department,
            "available": True,
            "current_patient": None
        }

        logger.info(
            f"Doctor registered: {doctor_id}"
        )

        return self.doctors[doctor_id]

    # =====================================================
    # SET UNAVAILABLE
    # =====================================================

    def set_unavailable(
        self,
        doctor_id: str,
        patient_id: str = None
    ):

        if doctor_id not in self.doctors:
            return None

        self.doctors[doctor_id]["available"] = False

        self.doctors[doctor_id][
            "current_patient"
        ] = patient_id

        logger.info(
            f"Doctor unavailable: {doctor_id}"
        )

        return self.doctors[doctor_id]

    # =====================================================
    # SET AVAILABLE
    # =====================================================

    def set_available(
        self,
        doctor_id: str
    ):

        if doctor_id not in self.doctors:
            return None

        self.doctors[doctor_id]["available"] = True

        self.doctors[doctor_id][
            "current_patient"
        ] = None

        logger.info(
            f"Doctor available: {doctor_id}"
        )

        return self.doctors[doctor_id]

    # =====================================================
    # GET AVAILABLE DOCTORS
    # =====================================================

    def get_available_doctors(
        self,
        department: str
    ):

        return [
            doctor
            for doctor in self.doctors.values()
            if doctor["department"] == department
            and doctor["available"] is True
        ]

    # =====================================================
    # GET SINGLE DOCTOR
    # =====================================================

    def get_doctor(
        self,
        doctor_id: str
    ):

        return self.doctors.get(doctor_id)

    # =====================================================
    # GET DEPARTMENT DOCTORS
    # =====================================================

    def get_department_doctors(
        self,
        department: str
    ):

        return [
            doctor
            for doctor in self.doctors.values()
            if doctor["department"] == department
        ]