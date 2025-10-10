import pytest

from gendiff import generate_diff
from gendiff.diff.parser import read_file


@pytest.mark.parametrize(
    "file1, file2",
    [
        (
            "tests/test_data/file1.json",
            "tests/test_data/file2.json",
        ),
        (
            "tests/test_data/file1.yaml",
            "tests/test_data/file2.yaml",
        ),
    ],
)
def test_generate_diff(file1, file2):
    expected_diff = read_file("tests/test_data/expected_json_diff.txt").strip()
    assert generate_diff(file1, file2).strip() == expected_diff
