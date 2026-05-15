from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class DataCleaning:

    def __init__(self):

        self.cleaned_records = 0

    # =====================================================
    # REMOVE NULL VALUES
    # =====================================================

    def remove_null_values(
        self,
        dataset: list
    ):

        cleaned = []

        for row in dataset:

            if all(
                value is not None
                for value in row.values()
            ):

                cleaned.append(row)

        logger.info(
            f"Null values removed: "
            f"{len(dataset) - len(cleaned)}"
        )

        return cleaned

    # =====================================================
    # REMOVE DUPLICATES
    # =====================================================

    def remove_duplicates(
        self,
        dataset: list,
        key: str
    ):

        seen = set()

        unique_rows = []

        for row in dataset:

            value = row.get(key)

            if value not in seen:

                seen.add(value)

                unique_rows.append(row)

        logger.info(
            f"Duplicates removed using key: "
            f"{key}"
        )

        return unique_rows

    # =====================================================
    # NORMALIZE STRINGS
    # =====================================================

    def normalize_strings(
        self,
        dataset: list
    ):

        normalized = []

        for row in dataset:

            cleaned_row = {}

            for key, value in row.items():

                if isinstance(value, str):

                    cleaned_row[key] = (
                        value
                        .strip()
                        .lower()
                    )

                else:

                    cleaned_row[key] = value

            normalized.append(cleaned_row)

        logger.info(
            "String normalization completed"
        )

        return normalized

    # =====================================================
    # COMPLETE CLEANING PIPELINE
    # =====================================================

    def clean_dataset(
        self,
        dataset: list,
        duplicate_key: str
    ):

        dataset = self.remove_null_values(
            dataset
        )

        dataset = self.remove_duplicates(
            dataset,
            duplicate_key
        )

        dataset = self.normalize_strings(
            dataset
        )

        self.cleaned_records = len(dataset)

        logger.info(
            "Dataset cleaning completed"
        )

        return dataset