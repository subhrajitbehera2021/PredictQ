from ai_engine.utils.logging_utils import (
    get_logger
)


logger = get_logger(__name__)


class DatasetUtils:

    @staticmethod
    def split_dataset(
        dataset: list,
        split_ratio: float = 0.8
    ):

        split_index = int(
            len(dataset) * split_ratio
        )

        train_data = dataset[:split_index]

        test_data = dataset[split_index:]

        logger.info(
            "Dataset split completed"
        )

        return {
            "train_data": train_data,
            "test_data": test_data
        }

    @staticmethod
    def get_dataset_size(
        dataset: list
    ):

        return len(dataset)

    @staticmethod
    def extract_column(
        dataset: list,
        column_name: str
    ):

        return [
            row.get(column_name)
            for row in dataset
            if column_name in row
        ]

    @staticmethod
    def generate_dataset_summary(
        dataset: list
    ):

        if not dataset:

            return {
                "total_rows": 0,
                "columns": []
            }

        columns = list(
            dataset[0].keys()
        )

        summary = {
            "total_rows": len(dataset),
            "columns": columns
        }

        logger.info(
            "Dataset summary generated"
        )

        return summary