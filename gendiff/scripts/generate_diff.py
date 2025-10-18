from gendiff.formatters.formatter import format_diff
from gendiff.scripts.diff_builder import build_diff
from gendiff.scripts.parser import parse_file


def generate_diff(file1: str, file2: str, format_name="stylish") -> str:
    parsed_data1, parsed_data2 = parse_file(file1), parse_file(file2)
    diff = build_diff(parsed_data1, parsed_data2)
    return format_diff(diff, format_name)
