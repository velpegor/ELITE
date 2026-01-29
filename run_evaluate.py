import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from elite_eval.config import (
    CSV_INPUT_PATH,
    EVAL_MODEL_NAME,
    IMAGE_BASE_DIR,
    MODEL_OUTPUT_COLUMNS,
    OUTPUT_JSONL_PATH,
)
from elite_eval.evaluate_batch import create_batch_file


def main():
    create_batch_file(
        csv_file_path=CSV_INPUT_PATH,
        output_file_path=OUTPUT_JSONL_PATH,
        image_base_dir=IMAGE_BASE_DIR,
        model_output_columns=MODEL_OUTPUT_COLUMNS,
        eval_model=EVAL_MODEL_NAME,
    )


if __name__ == "__main__":
    main()
