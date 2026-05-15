from collections import defaultdict

from ai_engine.utils.logging_utils import get_logger


logger = get_logger(__name__)


class EventDispatcher:

    def __init__(self):

        # {
        #   "PATIENT_REGISTERED": [func1, func2]
        # }

        self.listeners = defaultdict(list)

    # =====================================================
    # REGISTER EVENT LISTENER
    # =====================================================

    def subscribe(
        self,
        event_name: str,
        callback
    ):

        self.listeners[event_name].append(callback)

        logger.info(
            f"Listener subscribed to event: {event_name}"
        )

    # =====================================================
    # REMOVE EVENT LISTENER
    # =====================================================

    def unsubscribe(
        self,
        event_name: str,
        callback
    ):

        if event_name not in self.listeners:
            return

        if callback in self.listeners[event_name]:

            self.listeners[event_name].remove(callback)

            logger.info(
                f"Listener removed from event: {event_name}"
            )

    # =====================================================
    # DISPATCH EVENT
    # =====================================================

    def dispatch(
        self,
        event_name: str,
        payload=None
    ):

        logger.info(
            f"Dispatching event: {event_name}"
        )

        if event_name not in self.listeners:
            return

        for callback in self.listeners[event_name]:

            try:

                callback(payload)

            except Exception as error:

                logger.error(
                    f"Event callback error "
                    f"for {event_name}: {error}"
                )

    # =====================================================
    # CLEAR EVENT LISTENERS
    # =====================================================

    def clear_event(
        self,
        event_name: str
    ):

        if event_name in self.listeners:

            self.listeners[event_name] = []

            logger.info(
                f"Cleared listeners for {event_name}"
            )

    # =====================================================
    # CLEAR ALL EVENTS
    # =====================================================

    def clear_all(self):

        self.listeners.clear()

        logger.info(
            "All event listeners cleared"
        )

    # =====================================================
    # GET REGISTERED EVENTS
    # =====================================================

    def get_registered_events(self):

        return list(self.listeners.keys())

    # =====================================================
    # GET LISTENER COUNT
    # =====================================================

    def get_listener_count(
        self,
        event_name: str
    ):

        return len(
            self.listeners.get(event_name, [])
        )