from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class FeatureEngineering:

    def __init__(self):

        self.generated_features = 0

    # =====================================================
    # ETA FEATURES
    # =====================================================

    def build_eta_features(
        self,
        patient_record: dict
    ):

        features = {

            "queue_size":
            patient_record.get(
                "queue_size",
                0
            ),

            "available_doctors":
            patient_record.get(
                "available_doctors",
                1
            ),

            "patient_priority":
            patient_record.get(
                "priority",
                1
            ),

            "symptoms_count":
            len(
                patient_record.get(
                    "symptoms",
                    []
                )
            )
        }

        logger.info(
            "ETA features generated"
        )

        return features

    # =====================================================
    # NO-SHOW FEATURES
    # =====================================================

    def build_no_show_features(
        self,
        patient_record: dict
    ):

        features = {

            "previous_no_shows":
            patient_record.get(
                "previous_no_shows",
                0
            ),

            "travel_distance_km":
            patient_record.get(
                "travel_distance_km",
                0
            ),

            "waiting_time_minutes":
            patient_record.get(
                "waiting_time_minutes",
                0
            )
        }

        logger.info(
            "No-show features generated"
        )

        return features

    # =====================================================
    # CROWD FEATURES
    # =====================================================

    def build_crowd_features(
        self,
        department_record: dict
    ):

        features = {

            "patient_count":
            department_record.get(
                "patient_count",
                0
            ),

            "room_capacity":
            department_record.get(
                "room_capacity",
                1
            ),

            "doctor_count":
            department_record.get(
                "doctor_count",
                1
            )
        }

        logger.info(
            "Crowd features generated"
        )

        return features

    # =====================================================
    # GENERATE COMPLETE FEATURE SET
    # =====================================================

    def generate_feature_set(
        self,
        patient_record: dict,
        department_record: dict
    ):

        feature_set = {

            "eta_features":
            self.build_eta_features(
                patient_record
            ),

            "no_show_features":
            self.build_no_show_features(
                patient_record
            ),

            "crowd_features":
            self.build_crowd_features(
                department_record
            )
        }

        self.generated_features += 1

        logger.info(
            "Complete feature set generated"
        )

        return feature_set