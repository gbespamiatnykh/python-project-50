from json import dumps
from typing import Any


def format_json(diff: list[dict[str, Any]]) -> str:
    return dumps(diff, indent=4)
