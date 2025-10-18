from typing import Any


def plain_stringify(data: Any) -> str:
    if isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return "null"
    elif isinstance(data, dict):
        return "[complex value]"
    elif isinstance(data, str):
        return f"'{data}'"
    return str(data)


def format_plain(diff: list[dict[str, Any]], key_path="") -> str:
    text_lines = []
    for line in diff:
        key = line["key"]
        status = line["status"]
        value = plain_stringify(line["value"])
        old_value = plain_stringify(line.get("old_value"))
        match status:
            case "added":
                text_lines.append(
                    f"Property '{key_path}{key}' was "
                    f"{status} with value: {value}"
                )
            case "removed":
                text_lines.append(f"Property '{key_path}{key}' was {status}")
            case "nested":
                text_lines.append(
                    format_plain(line["value"], key_path + f"{key}.")
                )
            case "updated":
                text_lines.append(
                    f"Property '{key_path}{key}' was {status}. "
                    f"From {old_value} to {value}"
                )
    return "\n".join(text_lines)
