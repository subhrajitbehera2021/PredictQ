from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class RealtimeDecisionEngine:

    def __init__(self):

        self.decision_history = []

    # =====================================================
    # OVERLOAD DECISION
    # =====================================================

    def evaluate_overload(
        self,
        queue_size: int,
        threshold: int = 50
    ):

        overloaded = queue_size >= threshold

        logger.info(
            f"Overload evaluation: "
            f"{overloaded}"
        )

        return overloaded

    # =====================================================
    # DOCTOR REALLOCATION DECISION
    # =====================================================

    def decide_doctor_reallocation(
        self,
        overloaded_departments: list,
        available_departments: list
    ):

        decisions = []

        for overloaded in overloaded_departments:

            for available in available_departments:

                if overloaded != available:

                    decisions.append({

                        "action":
                        "REALLOCATE_DOCTOR",

                        "from_department":
                        available,

                        "to_department":
                        overloaded
                    })

        logger.info(
            f"Doctor reallocations generated: "
            f"{len(decisions)}"
        )

        return decisions

    # =====================================================
    # QUEUE REDIRECTION
    # =====================================================

    def decide_queue_redirection(
        self,
        queue_size: int,
        nearby_departments: list
    ):

        if queue_size < 40:

            return None

        if not nearby_departments:

            return None

        redirect_department = (
            nearby_departments[0]
        )

        decision = {

            "action":
            "REDIRECT_QUEUE",

            "redirect_to":
            redirect_department
        }

        logger.info(
            f"Queue redirection decision: "
            f"{redirect_department}"
        )

        return decision

    # =====================================================
    # CAPACITY EXPANSION DECISION
    # =====================================================

    def decide_capacity_expansion(
        self,
        predicted_load: int,
        available_doctors: int
    ):

        ratio = (
            predicted_load
            / max(available_doctors, 1)
        )

        if ratio >= 30:

            decision = {

                "action":
                "EXPAND_CAPACITY",

                "priority":
                "CRITICAL"
            }

            logger.warning(
                "Capacity expansion required"
            )

            return decision

        return None

    # =====================================================
    # COMPLETE DECISION WORKFLOW
    # =====================================================

    def generate_realtime_decisions(
        self,
        department_data: dict
    ):

        decisions = []

        overloaded_departments = []

        available_departments = []

        for department, data in (
            department_data.items()
        ):

            queue_size = data.get(
                "queue_size",
                0
            )

            available_doctors = data.get(
                "available_doctors",
                1
            )

            if self.evaluate_overload(
                queue_size
            ):

                overloaded_departments.append(
                    department
                )

            else:

                available_departments.append(
                    department
                )

            capacity_decision = (
                self.decide_capacity_expansion(
                    queue_size,
                    available_doctors
                )
            )

            if capacity_decision:

                decisions.append({
                    "department":
                    department,

                    **capacity_decision
                })

        reallocations = (
            self.decide_doctor_reallocation(
                overloaded_departments,
                available_departments
            )
        )

        decisions.extend(
            reallocations
        )

        self.decision_history.append(
            decisions
        )

        logger.info(
            "Realtime AI decisions generated"
        )

        return decisions

    # =====================================================
    # GET DECISION HISTORY
    # =====================================================

    def get_decision_history(self):

        return self.decision_history