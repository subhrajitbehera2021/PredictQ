from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class DatasetBuilder:

    def __init__(self):

        self.dataset_history = []

    # =====================================================
    # BUILD ETA DATASET
    # =====================================================

    def build_eta_dataset(
        self,
        feature_records: list
    ):

        dataset = []

        for record in feature_records:

            eta_features = (
                record.get(
                    "eta_features",
                    {}
                )
            )

            dataset.append({

                "queue_size":
                eta_features.get(
                    "queue_size",
                    0
                ),

                "available_doctors":
                eta_features.get(
                    "available_doctors",
                    1
                ),

                "patient_priority":
                eta_features.get(
                    "patient_priority",
                    1
                ),

                "symptoms_count":
                eta_features.get(
                    "symptoms_count",
                    0
                )
            })

        logger.info(
            "ETA dataset built"
        )

        return dataset

    # =====================================================
    # BUILD NO-SHOW DATASET
    # =====================================================

    def build_no_show_dataset(
        self,
        feature_records: list
    ):

        dataset = []

        for record in feature_records:

            no_show_features = (
                record.get(
                    "no_show_features",
                    {}
                )
            )

            dataset.append({

                "previous_no_shows":
                no_show_features.get(
                    "previous_no_shows",
                    0
                ),

                "travel_distance_km":
                no_show_features.get(
                    "travel_distance_km",
                    0
                ),

                "waiting_time_minutes":
                no_show_features.get(
                    "waiting_time_minutes",
                    0
                )
            })

        logger.info(
            "No-show dataset built"
        )

        return dataset

    # =====================================================
    # BUILD CROWD DATASET
    # =====================================================

    def build_crowd_dataset(
        self,
        feature_records: list
    ):

        dataset = []

        for record in feature_records:

            crowd_features = (
                record.get(
                    "crowd_features",
                    {}
                )
            )

            dataset.append({

                "patient_count":
                crowd_features.get(
                    "patient_count",
                    0
                ),

                "room_capacity":
                crowd_features.get(
                    "room_capacity",
                    1
                ),

                "doctor_count":
                crowd_features.get(
                    "doctor_count",
                    1
                )
            })

        logger.info(
            "Crowd dataset built"
        )

        return dataset

    # =====================================================
    # BUILD COMPLETE TRAINING DATASET
    # =====================================================

    def build_training_dataset(
        self,
        feature_records: list
    ):

        training_dataset = {

            "eta_dataset":
            self.build_eta_dataset(
                feature_records
            ),

            "no_show_dataset":
            self.build_no_show_dataset(
                feature_records
            ),

            "crowd_dataset":
            self.build_crowd_dataset(
                feature_records
            )
        }

        self.dataset_history.append(
            training_dataset
        )

        logger.info(
            "Training dataset generated"
        )

        return training_dataset

    # =====================================================
    # GET DATASET HISTORY
    # =====================================================

    def get_dataset_history(self):

        return self.dataset_history