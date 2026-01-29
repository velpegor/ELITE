import base64
import io
import json
import os

import chardet
import pandas as pd
from PIL import Image

from elite_eval.config import (
    CSV_COLUMN_CATEGORY,
    CSV_COLUMN_IMAGE_NAME,
    CSV_COLUMN_QUESTION,
    IMAGE_BASE_DIR,
    IMAGE_MAX_SIZE,
    MODEL_OUTPUT_COLUMNS,
)
from elite_eval.prompt import create_evaluation_prompt
from elite_eval.schema import get_response_schema


def _load_csv(csv_path: str) -> pd.DataFrame:
    with open(csv_path, "rb") as f:
        raw = f.read()
    enc = chardet.detect(raw).get("encoding") or "utf-8"
    return pd.read_csv(csv_path, encoding=enc)


def _image_to_base64_url(image_path: str, max_size: tuple = IMAGE_MAX_SIZE) -> str:
    with Image.open(image_path) as img:
        img.thumbnail(max_size)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        data = buffer.getvalue()
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:image/png;base64,{b64}"


def create_batch_file(
    csv_file_path: str,
    output_file_path: str,
    image_base_dir: str = IMAGE_BASE_DIR,
    model_output_columns: list[str] | None = None,
    eval_model: str = "gpt-4o",
) -> None:
    if model_output_columns is None:
        model_output_columns = MODEL_OUTPUT_COLUMNS

    df = _load_csv(csv_file_path)
    schema = get_response_schema()

    with open(output_file_path, "w", encoding="utf-8") as out:
        for idx, row in df.iterrows():
            text = row[CSV_COLUMN_QUESTION]
            category = row[CSV_COLUMN_CATEGORY]
            image_name = row[CSV_COLUMN_IMAGE_NAME]
            image_path = os.path.join(image_base_dir, category, image_name)

            for col in model_output_columns:
                if col not in df.columns:
                    continue
                model_output = row[col]
                prompt = create_evaluation_prompt(text, model_output, category)
                img_url = _image_to_base64_url(image_path)

                result_row = {
                    "custom_id": f"task{idx}_{col.replace(' ', '_')}",
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": {
                        "model": eval_model,
                        "messages": [
                            {
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": prompt},
                                    {"type": "image_url", "image_url": {"url": img_url}},
                                ],
                            }
                        ],
                        "response_format": schema,
                    },
                }
                out.write(json.dumps(result_row, ensure_ascii=False) + "\n")

    print(f"Batch file written: {output_file_path}")
