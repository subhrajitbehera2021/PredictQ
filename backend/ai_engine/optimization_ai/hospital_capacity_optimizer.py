from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class HospitalCapacityOptimizer:

    def __init__(self):

        self.optimization_history = []

    # =====================================================
    # ANALYZE CAPACITY STATUS
    # =====================================================

    def analyze_capacity(
        self,
        patient_load: int,
        doctor_count: int,
        room_count: int
    ):

        total_capacity = (
            (doctor_count * 15)
            + (room_count * 5)
        )

        utilization = 0

        if total_capacity > 0:

            utilization = (
                patient_load
                / total_capacity
            ) * 100

        utilization = round(
            utilization,
            2
        )

        # CAPACITY STATUS
        if utilization >= 90:

            status = "CRITICAL"

        elif utilization >= 70:

            status = "HIGH"

        elif utilization >= 40:

            status = "MEDIUM"

        else:

            status = "LOW"

        result = {

            "patient_load":
            patient_load,

            "doctor_count":
            doctor_count,

            "room_count":
            room_count,

            "total_capacity":
            total_capacity,

            "utilization_percentage":
            utilization,

            "capacity_status":
            status
        }

        self.optimization_history.append(
            result
        )

        logger.info(
            f"Capacity analyzed: "
            f"{status}"
        )

        return result

    # =====================================================
    # GENERATE RECOMMENDATIONS
    # =====================================================

    def generate_recommendations(
        self,
        utilization_percentage: float
    ):

        recommendations = []

        if utilization_percentage >= 90:

            recommendations.append(
                "Increase doctors immediately"
            )

            recommendations.append(
                "Open emergency waiting rooms"
            )

        elif utilization_percentage >= 70:

            recommendations.append(
                "Add temporary consultation slots"
            )

        elif utilization_percentage >= 40:

            recommendations.append(
                "Monitor patient inflow"
            )

        else:

            recommendations.append(
                "Capacity operating normally"
            )

        logger.info(
            "Capacity recommendations generated"
        )

        return recommendations

    # =====================================================
    # COMPLETE OPTIMIZATION REPORT
    # =====================================================

    def generate_optimization_report(
        self,
        patient_load: int,
        doctor_count: int,
        room_count: int
    ):

        analysis = self.analyze_capacity(
            patient_load,
            doctor_count,
            room_count
        )

        recommendations = (
            self.generate_recommendations(
                analysis[
                    "utilization_percentage"
                ]
            )
        )

        report = {

            "analysis":
            analysis,

            "recommendations":
            recommendations
        }

        logger.info(
            "Hospital optimization report generated"
        )

        return report

    # =====================================================
    # GET HISTORY
    # =====================================================

    def get_history(self):

        return self.optimization_history