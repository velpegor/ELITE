import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from elite_eval.config import BATCH_OUTPUT_JSONL, CSV_COLUMN_CATEGORY, CSV_INPUT_PATH
from elite_eval.metrics import compute_metrics, format_metrics


def main():
    path = os.environ.get("ELITE_BATCH_OUTPUT_JSONL", BATCH_OUTPUT_JSONL)
    csv_path = os.environ.get("ELITE_CSV_INPUT", CSV_INPUT_PATH)
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    if len(sys.argv) >= 3:
        csv_path = sys.argv[2]
    if not os.path.isfile(path):
        print(f"File not found: {path}")
        sys.exit(1)
    category_asr, overall_asr = compute_metrics(
        path,
        csv_path=csv_path if os.path.isfile(csv_path) else None,
        category_column=CSV_COLUMN_CATEGORY,
    )
    print(format_metrics(category_asr, overall_asr))


if __name__ == "__main__":
    main()
