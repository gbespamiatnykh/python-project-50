import argparse
import json
from typing import Any


def bool_to_lower_str(value) -> str | Any:
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(first_file: dict, second_file: dict) -> str:
    difference = ["{", "}"]
    for key in sorted(set(first_file) | set(second_file)):
        if key in first_file and key not in second_file:
            difference.insert(
                -1, f"  - {key}: {bool_to_lower_str(first_file[key])}"
                )
        elif key not in first_file and key in second_file:
            difference.insert(
                -1, f"  + {key}: {bool_to_lower_str(second_file[key])}"
                )
        elif first_file[key] != second_file[key]:
            difference.insert(
                -1,
                f"  - {key}: {bool_to_lower_str(first_file.get(key))}\n"
                f"  + {key}: {bool_to_lower_str(second_file[key])}"
            )
        else:
            difference.insert(
                -1, f"    {key}: {bool_to_lower_str(first_file[key])}"
                )
    return "\n".join(difference)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))
    print(generate_diff(first_file, second_file))


if __name__ == "__main__":
    main()
