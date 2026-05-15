from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class OperationalMetricsAI:

    def __init__(self):

        self.metrics_history = []

    # =====================================================
    # QUEUE EFFICIENCY
    # =====================================================

    def calculate_queue_efficiency(
        self,
        served_patients: int,
        total_patients: int
    ):

        if total_patients <= 0:
            return 0

        efficiency = (
            served_patients
            / total_patients
        ) * 100

        return round(efficiency, 2)

    # =====================================================
    # DOCTOR UTILIZATION
    # =====================================================

    def calculate_doctor_utilization(
        self,
        busy_doctors: int,
        total_doctors: int
    ):

        if total_doctors <= 0:
            return 0

        utilization = (
            busy_doctors
            / total_doctors
        ) * 100

        return round(utilization, 2)

    # =====================================================
    # PATIENT THROUGHPUT
    # =====================================================

    def calculate_patient_throughput(
        self,
        served_patients: int,
        operating_hours: int
    ):

        if operating_hours <= 0:
            return 0

        throughput = (
            served_patients
            / operating_hours
        )

        return round(throughput, 2)

    # =====================================================
    # OVERLOAD RATE
    # =====================================================

    def calculate_overload_rate(
        self,
        overloaded_departments: int,
        total_departments: int
    ):

        if total_departments <= 0:
            return 0

        overload_rate = (
            overloaded_departments
            / total_departments
        ) * 100

        return round(overload_rate, 2)

    # =====================================================
    # GENERATE METRICS REPORT
    # =====================================================

    def generate_operational_report(
        self,
        served_patients: int,
        total_patients: int,
        busy_doctors: int,
        total_doctors: int,
        operating_hours: int,
        overloaded_departments: int,
        total_departments: int
    ):

        report = {

            "queue_efficiency":
            self.calculate_queue_efficiency(
                served_patients,
                total_patients
            ),

            "doctor_utilization":
            self.calculate_doctor_utilization(
                busy_doctors,
                total_doctors
            ),

            "patient_throughput":
            self.calculate_patient_throughput(
                served_patients,
                operating_hours
            ),

            "overload_rate":
            self.calculate_overload_rate(
                overloaded_departments,
                total_departments
            )
        }

        self.metrics_history.append(
            report
        )

        logger.info(
            "Operational report generated"
        )

        return report

    # =====================================================
    # METRICS HISTORY
    # =====================================================

    def get_metrics_history(self):

        return self.metrics_history