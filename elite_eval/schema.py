def get_response_schema():
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "multiple_responses",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "question1": {
                        "type": "object",
                        "properties": {
                            "reasoning": {"type": "string"},
                            "value": {"type": "number"}
                        },
                        "required": ["reasoning", "value"],
                        "additionalProperties": False
                    },
                    "question2": {
                        "type": "object",
                        "properties": {
                            "reasoning": {"type": "string"},
                            "value": {"type": "number"}
                        },
                        "required": ["reasoning", "value"],
                        "additionalProperties": False
                    },
                    "question3": {
                        "type": "object",
                        "properties": {
                            "reasoning": {"type": "string"},
                            "value": {"type": "number"}
                        },
                        "required": ["reasoning", "value"],
                        "additionalProperties": False
                    },
                    "question4": {
                        "type": "object",
                        "properties": {
                            "reasoning": {"type": "string"},
                            "value": {"type": "number"}
                        },
                        "required": ["reasoning", "value"],
                        "additionalProperties": False
                    }
                },
                "required": ["question1", "question2", "question3", "question4"],
                "additionalProperties": False
            }
        }
    }
