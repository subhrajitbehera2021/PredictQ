from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class QueueBalancer:

    # =====================================================
    # GET DEPARTMENT LOADS
    # =====================================================

    def get_department_loads(
        self,
        departments: dict
    ):

        department_loads = {
            department: len(queue)
            for department, queue in departments.items()
        }

        logger.info(
            f"Department loads calculated"
        )

        return department_loads

    # =====================================================
    # FIND LEAST BUSY DEPARTMENT
    # =====================================================

    def find_least_busy_department(
        self,
        departments: dict
    ):

        department_loads = (
            self.get_department_loads(
                departments
            )
        )

        if not department_loads:

            logger.warning(
                "No departments available "
                "for balancing"
            )

            return None

        least_busy = min(
            department_loads,
            key=department_loads.get
        )

        logger.info(
            f"Least busy department: "
            f"{least_busy}"
        )

        return least_busy

    # =====================================================
    # BALANCE DEPARTMENTS
    # =====================================================

    def balance_departments(
        self,
        departments: dict
    ):

        department_loads = (
            self.get_department_loads(
                departments
            )
        )

        least_busy_department = (
            self.find_least_busy_department(
                departments
            )
        )

        logger.info(
            "Queue balancing completed"
        )

        return {
            "department_loads": department_loads,
            "least_busy_department": (
                least_busy_department
            )
        }