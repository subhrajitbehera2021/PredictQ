from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class AnomalyDetector:

    def __init__(self):

        self.detected_anomalies = []

    # =====================================================
    # QUEUE SPIKE DETECTION
    # =====================================================

    def detect_queue_spike(
        self,
        queue_size: int,
        threshold: int = 50
    ):

        detected = queue_size >= threshold

        if detected:

            anomaly = {
                "type": "QUEUE_SPIKE",
                "queue_size": queue_size
            }

            self.detected_anomalies.append(
                anomaly
            )

            logger.warning(
                f"Queue spike detected: "
                f"{queue_size}"
            )

        return detected

    # =====================================================
    # DOCTOR SHORTAGE DETECTION
    # =====================================================

    def detect_doctor_shortage(
        self,
        available_doctors: int
    ):

        detected = available_doctors <= 0

        if detected:

            anomaly = {
                "type": "DOCTOR_SHORTAGE",
                "available_doctors":
                available_doctors
            }

            self.detected_anomalies.append(
                anomaly
            )

            logger.warning(
                "Doctor shortage detected"
            )

        return detected

    # =====================================================
    # WAIT TIME ANOMALY
    # =====================================================

    def detect_wait_time_anomaly(
        self,
        wait_time: int,
        threshold: int = 120
    ):

        detected = wait_time >= threshold

        if detected:

            anomaly = {
                "type": "WAIT_TIME_ANOMALY",
                "wait_time": wait_time
            }

            self.detected_anomalies.append(
                anomaly
            )

            logger.warning(
                f"Abnormal wait time detected: "
                f"{wait_time}"
            )

        return detected

    # =====================================================
    # REALTIME FAILURE DETECTION
    # =====================================================

    def detect_realtime_failure(
        self,
        sync_active: bool
    ):

        detected = not sync_active

        if detected:

            anomaly = {
                "type": "REALTIME_FAILURE"
            }

            self.detected_anomalies.append(
                anomaly
            )

            logger.warning(
                "Realtime synchronization failure"
            )

        return detected

    # =====================================================
    # SYSTEM RISK ANALYSIS
    # =====================================================

    def generate_risk_report(
        self
    ):

        report = {

            "total_anomalies":
            len(self.detected_anomalies),

            "anomalies":
            self.detected_anomalies
        }

        logger.info(
            "System risk report generated"
        )

        return report

    # =====================================================
    # RESET DETECTOR
    # =====================================================

    def reset_anomalies(self):

        self.detected_anomalies = []

        logger.info(
            "Anomaly detector reset"
        )