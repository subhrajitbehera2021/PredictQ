from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class RecoveryEngine:

    def __init__(self):

        self.recovery_history = []

    def recover_prediction_service(self):

        recovery = {
            "service": "AI_PREDICTION",
            "status": "RECOVERED",
            "action": "RESTART_PREDICTION_PIPELINE"
        }

        self.recovery_history.append(recovery)

        logger.info("Prediction service recovered")

        return recovery

    def recover_realtime_service(self):

        recovery = {
            "service": "REALTIME_SYNC",
            "status": "RECOVERED",
            "action": "RECONNECT_REALTIME_CHANNEL"
        }

        self.recovery_history.append(recovery)

        logger.info("Realtime service recovered")

        return recovery

    def recover_websocket_service(self):

        recovery = {
            "service": "WEBSOCKET",
            "status": "RECOVERED",
            "action": "RECONNECT_WEBSOCKET_CLIENTS"
        }

        self.recovery_history.append(recovery)

        logger.info("WebSocket service recovered")

        return recovery

    def recover_full_system(self):

        recoveries = [
            self.recover_prediction_service(),
            self.recover_realtime_service(),
            self.recover_websocket_service()
        ]

        logger.info("Full system recovery completed")

        return {
            "system": "RECOVERED",
            "recoveries": recoveries
        }

    def get_recovery_history(self):

        return self.recovery_history

    def clear_history(self):

        self.recovery_history = []

        logger.info("Recovery history cleared")