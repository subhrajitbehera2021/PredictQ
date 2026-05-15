from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class DatabaseManager:

    def __init__(self):

        self.connected = False

        self.storage = {
            "patients": [],
            "predictions": [],
            "doctors": [],
            "audit_logs": []
        }

    # =====================================================
    # CONNECT DATABASE
    # =====================================================

    def connect(self):

        self.connected = True

        logger.info(
            "Database connected"
        )

        return {
            "status": "CONNECTED"
        }

    # =====================================================
    # SAVE PATIENT
    # =====================================================

    def save_patient(
        self,
        patient_data: dict
    ):

        self.storage[
            "patients"
        ].append(
            patient_data
        )

        logger.info(
            "Patient saved"
        )

        return {
            "saved": True
        }

    # =====================================================
    # SAVE PREDICTION
    # =====================================================

    def save_prediction(
        self,
        prediction_data: dict
    ):

        self.storage[
            "predictions"
        ].append(
            prediction_data
        )

        logger.info(
            "Prediction saved"
        )

        return {
            "saved": True
        }

    # =====================================================
    # SAVE DOCTOR
    # =====================================================

    def save_doctor(
        self,
        doctor_data: dict
    ):

        self.storage[
            "doctors"
        ].append(
            doctor_data
        )

        logger.info(
            "Doctor saved"
        )

        return {
            "saved": True
        }

    # =====================================================
    # SAVE AUDIT LOG
    # =====================================================

    def save_audit_log(
        self,
        log_data: dict
    ):

        self.storage[
            "audit_logs"
        ].append(
            log_data
        )

        logger.info(
            "Audit log saved"
        )

        return {
            "saved": True
        }

    # =====================================================
    # GET TABLE DATA
    # =====================================================

    def get_table_data(
        self,
        table_name: str
    ):

        return self.storage.get(
            table_name,
            []
        )

    # =====================================================
    # DATABASE STATUS
    # =====================================================

    def get_status(self):

        return {
            "connected": self.connected,
            "tables": list(
                self.storage.keys()
            )
        }