from ai_engine.utils.logging_utils import (
    get_logger
)

from ai_engine.monitoring.ai_health_monitor import (
    AIHealthMonitor
)

from ai_engine.monitoring.anomaly_detector import (
    AnomalyDetector
)

from ai_engine.fallback_system.degraded_mode_manager import (
    DegradedModeManager
)

from ai_engine.fallback_system.recovery_engine import (
    RecoveryEngine
)


logger = get_logger(__name__)


class SystemMonitor:

    def __init__(self):

        self.health_monitor = (
            AIHealthMonitor()
        )

        self.anomaly_detector = (
            AnomalyDetector()
        )

        self.degraded_manager = (
            DegradedModeManager()
        )

        self.recovery_engine = (
            RecoveryEngine()
        )

    # =====================================================
    # SYSTEM HEALTH CHECK
    # =====================================================

    def monitor_health(
        self,
        queue_size: int,
        available_doctors: int
    ):

        queue_status = (
            self.health_monitor
            .check_queue_pressure(
                queue_size
            )
        )

        doctor_status = (
            self.health_monitor
            .check_doctor_availability(
                available_doctors
            )
        )

        health = (
            self.health_monitor
            .get_system_health()
        )

        logger.info(
            "System health monitored"
        )

        return {
            "queue_status":
            queue_status,

            "doctor_status":
            doctor_status,

            "health":
            health
        }

    # =====================================================
    # ANOMALY MONITORING
    # =====================================================

    def monitor_anomalies(
        self,
        queue_size: int,
        available_doctors: int
    ):

        self.anomaly_detector.detect_queue_spike(
            queue_size
        )

        self.anomaly_detector.detect_doctor_shortage(
            available_doctors
        )

        report = (
            self.anomaly_detector
            .generate_risk_report()
        )

        logger.info(
            "Anomaly monitoring completed"
        )

        return report

    # =====================================================
    # DEGRADED MODE ACTIVATION
    # =====================================================

    def activate_degraded_mode(
        self,
        reason: str
    ):

        status = (
            self.degraded_manager
            .activate_degraded_mode(
                reason
            )
        )

        logger.warning(
            "System entered degraded mode"
        )

        return status

    # =====================================================
    # SYSTEM RECOVERY
    # =====================================================

    def recover_system(self):

        recovery = (
            self.recovery_engine
            .recover_full_system()
        )

        self.degraded_manager.deactivate_degraded_mode()

        logger.info(
            "System fully recovered"
        )

        return recovery

    # =====================================================
    # COMPLETE MONITORING REPORT
    # =====================================================

    def generate_monitoring_report(
        self,
        queue_size: int,
        available_doctors: int
    ):

        health_report = (
            self.monitor_health(
                queue_size,
                available_doctors
            )
        )

        anomaly_report = (
            self.monitor_anomalies(
                queue_size,
                available_doctors
            )
        )

        degraded_status = (
            self.degraded_manager
            .get_status()
        )

        report = {

            "health":
            health_report,

            "anomalies":
            anomaly_report,

            "degraded_mode":
            degraded_status
        }

        logger.info(
            "Monitoring report generated"
        )

        return report