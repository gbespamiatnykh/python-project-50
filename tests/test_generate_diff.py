import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, expected_diff_path",
    [
        (
            "tests/test_data/file1.json",
            "tests/test_data/file2.json",
            "tests/test_data/expected_json_diff.txt",
        )
    ],
)
def test_generate_diff(file1, file2, expected_diff_path):
    with open(expected_diff_path, "r", encoding="utf-8") as expected_data:
        expected_diff = expected_data.read().strip()
    assert generate_diff(file1, file2).strip() == expected_diff
