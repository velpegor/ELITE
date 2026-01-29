import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from elite_eval.config import BATCH_COMPLETION_WINDOW, OUTPUT_JSONL_PATH
from elite_eval.submit_batch import submit_batch


def main():
    submit_batch(
        jsonl_path=OUTPUT_JSONL_PATH,
        completion_window=BATCH_COMPLETION_WINDOW,
        description="ELITE evaluation batch",
    )


if __name__ == "__main__":
    main()
