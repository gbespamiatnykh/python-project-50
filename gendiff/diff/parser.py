import json
from pathlib import Path
from typing import Any

import yaml

TEST_DATA_DIR = "tests/test_data"


def get_file_path(filename: str) -> Path:
    path = Path(filename)
    if path.is_absolute() or path.exists():
        return path
    return path.parent / TEST_DATA_DIR / filename


def read_file(file_path: Path) -> str:
    with open(file_path, encoding="utf-8") as file:
        return file.read()


def get_format(file_path: Path) -> str:
    return file_path.suffix.lower()


def parse_data(data: str, format: str) -> dict[str, Any]:
    if format == ".json":
        return json.loads(data)
    elif format in (".yml", ".yaml"):
        return yaml.safe_load(data)
    raise ValueError(f"Unsupported file format: {format}")


def parse_file(file_name: str) -> dict[str, Any]:
    file_path = get_file_path(file_name)
    data = read_file(file_path)
    format = get_format(file_path)
    return parse_data(data, format)
