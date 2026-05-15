from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class ResourceAllocator:

    def __init__(self):

        self.allocation_history = []

    # =====================================================
    # ANALYZE DEPARTMENT LOADS
    # =====================================================

    def analyze_department_loads(
        self,
        department_data: dict
    ):

        loads = {}

        for department, data in (
            department_data.items()
        ):

            doctors = max(
                data.get(
                    "available_doctors",
                    1
                ),
                1
            )

            load_ratio = (
                data.get("queue_size", 0)
                / doctors
            )

            loads[department] = round(
                load_ratio,
                2
            )

        logger.info(
            "Department loads analyzed"
        )

        return loads

    # =====================================================
    # FIND OVERLOADED DEPARTMENTS
    # =====================================================

    def find_overloaded_departments(
        self,
        department_data: dict,
        threshold: int = 10
    ):

        loads = self.analyze_department_loads(
            department_data
        )

        overloaded = [

            department

            for department, ratio
            in loads.items()

            if ratio >= threshold
        ]

        logger.info(
            f"Overloaded departments: "
            f"{len(overloaded)}"
        )

        return overloaded

    # =====================================================
    # FIND UNDERUTILIZED DEPARTMENTS
    # =====================================================

    def find_underutilized_departments(
        self,
        department_data: dict,
        threshold: int = 3
    ):

        loads = self.analyze_department_loads(
            department_data
        )

        underutilized = [

            department

            for department, ratio
            in loads.items()

            if ratio <= threshold
        ]

        logger.info(
            f"Underutilized departments: "
            f"{len(underutilized)}"
        )

        return underutilized

    # =====================================================
    # GENERATE REALLOCATION PLAN
    # =====================================================

    def generate_reallocation_plan(
        self,
        department_data: dict
    ):

        overloaded = (
            self.find_overloaded_departments(
                department_data
            )
        )

        underutilized = (
            self.find_underutilized_departments(
                department_data
            )
        )

        reallocations = []

        for overloaded_department in overloaded:

            for available_department in underutilized:

                if (
                    overloaded_department
                    != available_department
                ):

                    reallocations.append({

                        "from_department":
                        available_department,

                        "to_department":
                        overloaded_department,

                        "action":
                        "REALLOCATE_DOCTOR"
                    })

        logger.info(
            "Resource reallocation plan generated"
        )

        self.allocation_history.append(
            reallocations
        )

        return reallocations

    # =====================================================
    # GET ALLOCATION HISTORY
    # =====================================================

    def get_allocation_history(self):

        return self.allocation_history