from ai_engine.utils.logging_utils import get_logger


logger = get_logger(__name__)


class RuntimeManager:

    def __init__(self):
        self.running = False

    def start(self):
        logger.info("Starting QueueSense AI Engine")
        self.running = True

    def shutdown(self):
        logger.info("Stopping QueueSense AI Engine")
        self.running = False