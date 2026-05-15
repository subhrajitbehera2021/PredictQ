from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class HospitalInsightsAI:

    def __init__(self):

        self.insights_cache = {}

    # =====================================================
    # BUSIEST DEPARTMENT
    # =====================================================

    def get_busiest_department(
        self,
        department_data: dict
    ):

        if not department_data:
            return None

        busiest = max(
            department_data,
            key=lambda dept:
            department_data[dept]["queue_size"]
        )

        logger.info(
            f"Busiest department analyzed: "
            f"{busiest}"
        )

        return busiest

    # =====================================================
    # OVERLOADED DEPARTMENTS
    # =====================================================

    def detect_overloaded_departments(
        self,
        department_data: dict,
        threshold: int = 30
    ):

        overloaded = []

        for department, data in (
            department_data.items()
        ):

            if data["queue_size"] >= threshold:

                overloaded.append(
                    department
                )

        logger.info(
            f"Overloaded departments detected: "
            f"{len(overloaded)}"
        )

        return overloaded

    # =====================================================
    # DOCTOR SHORTAGE ANALYSIS
    # =====================================================

    def detect_doctor_shortage(
        self,
        department_data: dict
    ):

        shortages = []

        for department, data in (
            department_data.items()
        ):

            if (
                data["available_doctors"]
                <= 1
            ):

                shortages.append(
                    department
                )

        logger.info(
            f"Doctor shortages detected: "
            f"{len(shortages)}"
        )

        return shortages

    # =====================================================
    # SMART RECOMMENDATIONS
    # =====================================================

    def generate_recommendations(
        self,
        department_data: dict
    ):

        recommendations = []

        overloaded = (
            self.detect_overloaded_departments(
                department_data
            )
        )

        shortages = (
            self.detect_doctor_shortage(
                department_data
            )
        )

        if overloaded:

            recommendations.append(
                "Increase OPD capacity in overloaded departments"
            )

        if shortages:

            recommendations.append(
                "Assign additional doctors to critical departments"
            )

        if not recommendations:

            recommendations.append(
                "Hospital operations are stable"
            )

        logger.info(
            "Hospital recommendations generated"
        )

        return recommendations

    # =====================================================
    # COMPLETE INSIGHTS REPORT
    # =====================================================

    def generate_hospital_insights(
        self,
        department_data: dict
    ):

        insights = {

            "busiest_department":
            self.get_busiest_department(
                department_data
            ),

            "overloaded_departments":
            self.detect_overloaded_departments(
                department_data
            ),

            "doctor_shortages":
            self.detect_doctor_shortage(
                department_data
            ),

            "recommendations":
            self.generate_recommendations(
                department_data
            )
        }

        self.insights_cache = insights

        logger.info(
            "Hospital insights report generated"
        )

        return insights

    # =====================================================
    # GET LAST INSIGHTS
    # =====================================================

    def get_cached_insights(self):

        return self.insights_cache