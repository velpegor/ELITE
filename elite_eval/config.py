import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
DATA_DIR = os.environ.get("ELITE_DATA_DIR", "data")
IMAGE_BASE_DIR = os.environ.get("ELITE_IMAGE_BASE_DIR", os.path.join(DATA_DIR, "images"))
CSV_INPUT_PATH = os.environ.get("ELITE_CSV_INPUT", os.path.join(DATA_DIR, "input.csv"))
OUTPUT_JSONL_PATH = os.environ.get("ELITE_OUTPUT_JSONL", "output.jsonl")
BATCH_OUTPUT_JSONL = os.environ.get("ELITE_BATCH_OUTPUT_JSONL", "batch_output.jsonl")
EVAL_MODEL_NAME = os.environ.get("ELITE_EVAL_MODEL", "gpt-4o")
BATCH_COMPLETION_WINDOW = os.environ.get("ELITE_BATCH_WINDOW", "24h")
MODEL_OUTPUT_COLUMNS = [
    c.strip() for c in os.environ.get("ELITE_MODEL_COLUMNS", "model_output").split(",")
]

CSV_COLUMN_QUESTION = os.environ.get("ELITE_CSV_COLUMN_QUESTION", "question")
CSV_COLUMN_CATEGORY = os.environ.get("ELITE_CSV_COLUMN_CATEGORY", "category_assigned")
CSV_COLUMN_IMAGE_NAME = os.environ.get("ELITE_CSV_COLUMN_IMAGE_NAME", "image_name")
IMAGE_MAX_SIZE = (256, 256)
