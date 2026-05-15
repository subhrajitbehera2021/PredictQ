from statistics import mean

from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class DoctorPerformanceAI:

    def __init__(self):

        self.performance_cache = {}

    # =====================================================
    # CONSULTATION SPEED
    # =====================================================

    def analyze_consultation_speed(
        self,
        consultation_times: list
    ):

        if not consultation_times:

            return {
                "average_consultation_time": 0
            }

        average_time = round(
            mean(consultation_times),
            2
        )

        logger.info(
            f"Average consultation time: "
            f"{average_time}"
        )

        return {
            "average_consultation_time":
            average_time
        }

    # =====================================================
    # PATIENT THROUGHPUT
    # =====================================================

    def analyze_patient_throughput(
        self,
        patients_completed: int,
        working_hours: int
    ):

        if working_hours <= 0:

            return {
                "patients_per_hour": 0
            }

        throughput = round(
            patients_completed
            / working_hours,
            2
        )

        logger.info(
            f"Doctor throughput analyzed: "
            f"{throughput}"
        )

        return {
            "patients_per_hour":
            throughput
        }

    # =====================================================
    # WORKLOAD ANALYSIS
    # =====================================================

    def analyze_workload(
        self,
        active_patients: int
    ):

        if active_patients >= 30:

            workload = "OVERLOADED"

        elif active_patients >= 15:

            workload = "BUSY"

        else:

            workload = "NORMAL"

        logger.info(
            f"Doctor workload: {workload}"
        )

        return {
            "workload_status":
            workload
        }

    # =====================================================
    # PERFORMANCE SCORE
    # =====================================================

    def generate_performance_score(
        self,
        consultation_time: float,
        throughput: float
    ):

        if consultation_time <= 0:

            return 0

        score = round(
            throughput
            * (60 / consultation_time),
            2
        )

        logger.info(
            f"Doctor performance score: "
            f"{score}"
        )

        return score

    # =====================================================
    # COMPLETE DOCTOR ANALYTICS
    # =====================================================

    def analyze_doctor_performance(
        self,
        doctor_id: str,
        consultation_times: list,
        patients_completed: int,
        working_hours: int,
        active_patients: int
    ):

        consultation_analysis = (
            self.analyze_consultation_speed(
                consultation_times
            )
        )

        throughput_analysis = (
            self.analyze_patient_throughput(
                patients_completed,
                working_hours
            )
        )

        workload_analysis = (
            self.analyze_workload(
                active_patients
            )
        )

        performance_score = (
            self.generate_performance_score(
                consultation_analysis[
                    "average_consultation_time"
                ],
                throughput_analysis[
                    "patients_per_hour"
                ]
            )
        )

        report = {

            "doctor_id":
            doctor_id,

            "consultation_metrics":
            consultation_analysis,

            "throughput_metrics":
            throughput_analysis,

            "workload_metrics":
            workload_analysis,

            "performance_score":
            performance_score
        }

        self.performance_cache[
            doctor_id
        ] = report

        logger.info(
            f"Doctor analytics completed "
            f"for {doctor_id}"
        )

        return report

    # =====================================================
    # GET CACHED PERFORMANCE
    # =====================================================

    def get_cached_performance(
        self,
        doctor_id: str
    ):

        return self.performance_cache.get(
            doctor_id,
            {}
        )