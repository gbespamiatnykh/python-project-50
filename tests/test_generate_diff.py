import pytest

from gendiff import generate_diff
from gendiff.diff.parser import read_file


@pytest.mark.parametrize(
    "file1, file2, expected_diff_file, format",
    [
        (
            "tests/test_data/file1.json",
            "tests/test_data/file2.json",
            "tests/test_data/expected_stylish_diff1.txt",
            "stylish",
        ),
        (
            "tests/test_data/file1.yaml",
            "tests/test_data/file2.yaml",
            "tests/test_data/expected_stylish_diff1.txt",
            "stylish",
        ),
        (
            "tests/test_data/file3.json",
            "tests/test_data/file4.json",
            "tests/test_data/expected_stylish_diff2.txt",
            "stylish",
        ),
        (
            "tests/test_data/file3.yaml",
            "tests/test_data/file4.yaml",
            "tests/test_data/expected_stylish_diff2.txt",
            "stylish",
        ),
        (
            "tests/test_data/file3.json",
            "tests/test_data/file4.json",
            "tests/test_data/expected_plain_diff.txt",
            "plain",
        ),
    ],
)
def test_generate_diff(file1, file2, expected_diff_file, format):
    expected_diff = read_file(expected_diff_file).strip()
    assert generate_diff(file1, file2, format).strip() == expected_diff
