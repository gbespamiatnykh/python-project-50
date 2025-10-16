from typing import Any

from gendiff.formatter.json import format_json
from gendiff.formatter.plain import format_plain
from gendiff.formatter.stylish import format_stylish


def format_diff(diff: list[dict[str, Any]], format_name: str) -> str:
    match format_name:
        case "stylish":
            return format_stylish(diff)
        case "plain":
            return format_plain(diff)
        case "json":
            return format_json(diff)
