from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class UtilizationAnalysis:

    def __init__(self):

        self.analysis_history = []

    # =====================================================
    # DOCTOR UTILIZATION
    # =====================================================

    def analyze_doctor_utilization(
        self,
        consultation_hours: float,
        available_hours: float
    ):

        if available_hours <= 0:
            return 0

        utilization = (
            consultation_hours
            / available_hours
        ) * 100

        return round(utilization, 2)

    # =====================================================
    # ROOM UTILIZATION
    # =====================================================

    def analyze_room_utilization(
        self,
        occupied_rooms: int,
        total_rooms: int
    ):

        if total_rooms <= 0:
            return 0

        utilization = (
            occupied_rooms
            / total_rooms
        ) * 100

        return round(utilization, 2)

    # =====================================================
    # DEPARTMENT UTILIZATION
    # =====================================================

    def analyze_department_utilization(
        self,
        active_patients: int,
        max_capacity: int
    ):

        if max_capacity <= 0:
            return 0

        utilization = (
            active_patients
            / max_capacity
        ) * 100

        return round(utilization, 2)

    # =====================================================
    # RESOURCE UTILIZATION
    # =====================================================

    def analyze_resource_utilization(
        self,
        used_resources: int,
        total_resources: int
    ):

        if total_resources <= 0:
            return 0

        utilization = (
            used_resources
            / total_resources
        ) * 100

        return round(utilization, 2)

    # =====================================================
    # GENERATE UTILIZATION REPORT
    # =====================================================

    def generate_utilization_report(
        self,
        consultation_hours: float,
        available_hours: float,
        occupied_rooms: int,
        total_rooms: int,
        active_patients: int,
        max_capacity: int,
        used_resources: int,
        total_resources: int
    ):

        report = {

            "doctor_utilization":
            self.analyze_doctor_utilization(
                consultation_hours,
                available_hours
            ),

            "room_utilization":
            self.analyze_room_utilization(
                occupied_rooms,
                total_rooms
            ),

            "department_utilization":
            self.analyze_department_utilization(
                active_patients,
                max_capacity
            ),

            "resource_utilization":
            self.analyze_resource_utilization(
                used_resources,
                total_resources
            )
        }

        self.analysis_history.append(
            report
        )

        logger.info(
            "Utilization analysis generated"
        )

        return report

    # =====================================================
    # GET ANALYSIS HISTORY
    # =====================================================

    def get_analysis_history(self):

        return self.analysis_history