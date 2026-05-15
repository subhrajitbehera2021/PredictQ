from typing import Dict
from uuid import uuid4

from ai_engine.utils.time_utils import TimeUtils
from ai_engine.utils.logging_utils import get_logger

from ai_engine.patient_ai.patient_priority_engine import (
    PatientPriorityEngine
)

from ai_engine.exceptions import (
    InvalidDepartmentException
)


logger = get_logger(__name__)


class WorkflowEngine:

    def __init__(
        self,
        state_manager,
        doctor_engine,
        queue_builder,
        wait_predictor
    ):

        self.state_manager = state_manager

        self.doctor_engine = doctor_engine

        self.queue_builder = queue_builder

        self.wait_predictor = wait_predictor

        self.priority_engine = PatientPriorityEngine()

    # =====================================================
    # MAIN PATIENT REGISTRATION WORKFLOW
    # =====================================================

    def process_patient_registration(
        self,
        department: str,
        patient_data: Dict
    ):

        logger.info(
            f"Processing patient registration for {department}"
        )

        # VALIDATE DEPARTMENT
        self.validate_department(
            department
        )

        # NORMALIZE PATIENT DATA
        normalized_patient = (
            self.normalize_patient_data(
                patient_data
            )
        )

        # ATTACH METADATA
        enriched_patient = (
            self.attach_patient_metadata(
                normalized_patient
            )
        )

        # ASSIGN PRIORITY
        prioritized_patient = (
            self.assign_priority(
                enriched_patient
            )
        )

        # INSERT INTO QUEUE
        queue = self.queue_builder.enqueue_patient(
            department,
            prioritized_patient
        )

        # CALCULATE POSITION
        position = self.calculate_queue_position(
            department,
            prioritized_patient["patient_id"]
        )

        # GENERATE ETA
        eta = self.generate_wait_estimation(
            department
        )

        response = {
            "success": True,
            "department": department,
            "patient": prioritized_patient,
            "queue_position": position,
            "estimated_wait_minutes": eta,
            "queue_size": len(queue)
        }

        logger.info(
            f"Patient queued successfully: "
            f"{prioritized_patient['patient_id']}"
        )

        return response

    # =====================================================
    # DEPARTMENT VALIDATION
    # =====================================================

    def validate_department(
        self,
        department: str
    ):

        if department not in self.state_manager.departments:

            raise InvalidDepartmentException(
                f"Department '{department}' "
                f"does not exist"
            )

    # =====================================================
    # NORMALIZE PATIENT DATA
    # =====================================================

    def normalize_patient_data(
        self,
        patient_data: Dict
    ):

        normalized = {

            "patient_id": patient_data.get(
                "patient_id",
                str(uuid4())
            ),

            "name": patient_data.get(
                "name",
                "Unknown"
            ),

            "age": patient_data.get(
                "age",
                30
            ),

            "gender": patient_data.get(
                "gender",
                "unknown"
            ),

            "disability": patient_data.get(
                "disability",
                False
            ),

            "symptoms": patient_data.get(
                "symptoms",
                []
            ),

            "priority": 1
        }

        return normalized

    # =====================================================
    # METADATA ENRICHMENT
    # =====================================================

    def attach_patient_metadata(
        self,
        patient_data: Dict
    ):

        patient_data["created_at"] = (
            TimeUtils.now()
        )

        patient_data["status"] = "WAITING"

        patient_data["workflow_version"] = "1.0"

        return patient_data

    # =====================================================
    # PRIORITY ASSIGNMENT
    # =====================================================

    def assign_priority(
        self,
        patient_data: Dict
    ):

        priority = (
            self.priority_engine
            .calculate_priority(
                patient_data
            )
        )

        patient_data["priority"] = (
            priority
        )

        return patient_data

    # =====================================================
    # CALCULATE QUEUE POSITION
    # =====================================================

    def calculate_queue_position(
        self,
        department: str,
        patient_id: str
    ):

        queue = (
            self.state_manager
            .get_department_queue(
                department
            )
        )

        for index, patient in enumerate(queue):

            if patient["patient_id"] == patient_id:

                return index + 1

        return -1

    # =====================================================
    # ETA GENERATION
    # =====================================================

    def generate_wait_estimation(
        self,
        department: str
    ):

        queue = (
            self.state_manager
            .get_department_queue(
                department
            )
        )

        doctors = (
            self.doctor_engine
            .get_available_doctors(
                department
            )
        )

        eta = self.wait_predictor.predict(
            queue_length=len(queue),
            available_doctors=len(doctors)
        )

        return eta

    # =====================================================
    # NEXT PATIENT WORKFLOW
    # =====================================================

    def process_next_patient(
        self,
        department: str
    ):

        queue = (
            self.state_manager
            .get_department_queue(
                department
            )
        )

        if not queue:

            logger.warning(
                f"No patients in queue for "
                f"{department}"
            )

            return None

        # POP NEXT PATIENT
        patient = queue.pop(0)

        patient["status"] = "IN_PROGRESS"

        # FIND AVAILABLE DOCTOR
        available_doctors = (
            self.doctor_engine
            .get_available_doctors(
                department
            )
        )

        assigned_doctor = None

        if available_doctors:

            assigned_doctor = available_doctors[0]

            self.doctor_engine.set_unavailable(
                assigned_doctor["doctor_id"],
                patient["patient_id"]
            )

        response = {
            "patient": patient,
            "assigned_doctor": assigned_doctor,
            "department": department
        }

        logger.info(
            f"Patient called: "
            f"{patient['patient_id']}"
        )

        return response

    # =====================================================
    # COMPLETE CONSULTATION
    # =====================================================

    def complete_consultation(
        self,
        doctor_id: str,
        patient_id: str
    ):

        self.doctor_engine.set_available(
            doctor_id
        )

        logger.info(
            f"Consultation completed for "
            f"patient {patient_id}"
        )

        return {
            "success": True,
            "doctor_id": doctor_id,
            "patient_id": patient_id,
            "status": "COMPLETED"
        }

    # =====================================================
    # GET DEPARTMENT SNAPSHOT
    # =====================================================

    def get_department_snapshot(
        self,
        department: str
    ):

        queue = (
            self.state_manager
            .get_department_queue(
                department
            )
        )

        available_doctors = (
            self.doctor_engine
            .get_available_doctors(
                department
            )
        )

        return {
            "department": department,
            "queue_size": len(queue),
            "available_doctors": len(
                available_doctors
            ),
            "patients": queue
        }

    # =====================================================
    # SYSTEM HEALTH SUMMARY
    # =====================================================

    def system_summary(self):

        summary = {}

        for department in (
            self.state_manager.departments
        ):

            queue = (
                self.state_manager
                .get_department_queue(
                    department
                )
            )

            doctors = (
                self.doctor_engine
                .get_available_doctors(
                    department
                )
            )

            summary[department] = {
                "queue_size": len(queue),
                "available_doctors": len(
                    doctors
                )
            }

        return summary