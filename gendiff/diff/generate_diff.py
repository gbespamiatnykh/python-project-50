from typing import Any

from gendiff.diff.parser import parse_file


def bool_to_lower_str(value: Any) -> Any:
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(first_file: str, second_file: str) -> str:
    parsed_data1 = parse_file(first_file)
    parsed_data2 = parse_file(second_file)
    difference = []
    merged_keys = sorted(set(parsed_data1) | set(parsed_data2))
    for key in merged_keys:
        if key in parsed_data1 and key not in parsed_data2:
            difference.append(
                f"  - {key}: {bool_to_lower_str(parsed_data1[key])}"
                )
        elif key not in parsed_data1 and key in parsed_data2:
            difference.append(
                f"  + {key}: {bool_to_lower_str(parsed_data2[key])}"
                )
        elif parsed_data1[key] != parsed_data2[key]:
            difference.append(
                f"  - {key}: {bool_to_lower_str(parsed_data1[key])}\n"
                f"  + {key}: {bool_to_lower_str(parsed_data2[key])}",
            )
        else:
            difference.append(
                f"    {key}: {bool_to_lower_str(parsed_data1[key])}"
                )
    return f"{{\n{"\n".join(difference)}\n}}"
