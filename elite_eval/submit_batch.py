import sys

from openai import OpenAI

from elite_eval.config import (
    BATCH_COMPLETION_WINDOW,
    OPENAI_API_KEY,
    OUTPUT_JSONL_PATH,
)


def submit_batch(
    jsonl_path: str = OUTPUT_JSONL_PATH,
    api_key: str | None = None,
    completion_window: str = BATCH_COMPLETION_WINDOW,
    description: str = "ELITE evaluation batch",
) -> str:
    key = api_key or OPENAI_API_KEY
    if not key:
        raise ValueError(
            "OpenAI API key is required. Set OPENAI_API_KEY in the environment or pass api_key."
        )

    client = OpenAI(api_key=key)

    with open(jsonl_path, "rb") as f:
        batch_input = client.files.create(file=f, purpose="batch")

    batch = client.batches.create(
        input_file_id=batch_input.id,
        endpoint="/v1/chat/completions",
        completion_window=completion_window,
        metadata={"description": description},
    )

    print(f"Batch input file ID: {batch_input.id}")
    print(f"Batch ID: {batch.id}")
    return batch.id


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_JSONL_PATH
    submit_batch(jsonl_path=path)
