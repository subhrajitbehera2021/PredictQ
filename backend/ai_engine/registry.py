from ai_engine.engine import (
    AIQueueEngine
)

from ai_engine.settings import (
    settings
)

from ai_engine.bootstrap import (
    bootstrap
)


class EngineRegistry:

    def __init__(self):

        self._registry = {}

    # =====================================================
    # REGISTER COMPONENT
    # =====================================================

    def register(
        self,
        component_name: str,
        component
    ):

        self._registry[
            component_name
        ] = component

        return True

    # =====================================================
    # GET COMPONENT
    # =====================================================

    def get(
        self,
        component_name: str
    ):

        return self._registry.get(
            component_name
        )

    # =====================================================
    # REMOVE COMPONENT
    # =====================================================

    def remove(
        self,
        component_name: str
    ):

        if component_name in self._registry:

            del self._registry[
                component_name
            ]

            return True

        return False

    # =====================================================
    # LIST COMPONENTS
    # =====================================================

    def list_components(self):

        return list(
            self._registry.keys()
        )

    # =====================================================
    # CLEAR REGISTRY
    # =====================================================

    def clear(self):

        self._registry.clear()

        return True

    # =====================================================
    # REGISTRY SIZE
    # =====================================================

    def size(self):

        return len(
            self._registry
        )


# =====================================================
# GLOBAL REGISTRY
# =====================================================

registry = EngineRegistry()

# =====================================================
# REGISTER CORE COMPONENTS
# =====================================================

registry.register(
    "engine",
    AIQueueEngine
)

registry.register(
    "settings",
    settings
)

registry.register(
    "bootstrap",
    bootstrap
)