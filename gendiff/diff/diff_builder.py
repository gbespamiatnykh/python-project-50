from typing import Any


def build_diff_line(
    key: str, status: str, value: Any, old_value=None
) -> dict[str, Any]:
    diff_line = {
        "key": key,
        "status": status,
        "value": value,
    }
    if status == "updated":
        diff_line["old_value"] = old_value
    return diff_line


def build_diff(
    data1: dict[str, Any], data2: dict[str, Any]
) -> list[dict[str, Any]]:
    merged_keys = sorted(set(data1) | set(data2))
    diff = []
    for key in merged_keys:
        value1, value2 = data1.get(key), data2.get(key)
        if key not in data1 and key in data2:
            diff.append(build_diff_line(key, "added", value2))
        elif key in data1 and key not in data2:
            diff.append(build_diff_line(key, "removed", value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(
                build_diff_line(key, "nested", build_diff(value1, value2))
            )
        elif value1 != value2:
            diff.append(build_diff_line(key, "updated", value2, value1))
        else:
            diff.append(build_diff_line(key, "unchanged", value1))
    return sorted(diff, key=lambda line: line["key"])
