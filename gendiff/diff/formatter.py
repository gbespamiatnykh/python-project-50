from typing import Any

INDENT_UNIT = ' '
LEVEL_LENGTH = 4
PREFIX = {
    'added': '+ ',
    'removed': '- ',
}
PREFIX_LENGTH = 2


def stylish_stringify(data: Any, level=1) -> str:
    if isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    elif isinstance(data, dict):
        indent_length = LEVEL_LENGTH * level
        lines = [
            f"{indent_length * INDENT_UNIT}{key}: "
            f"{stylish_stringify(value, level + 1)}"
            for key, value in data.items()
            ]
        bracket_indent = LEVEL_LENGTH * (level - 1) * INDENT_UNIT
        return f"{{\n{'\n'.join(lines)}\n{bracket_indent}}}"
    return str(data)


def format_stylish(diff: list[dict[str, Any]], level=1) -> str:
    text_lines = []
    indent_length = LEVEL_LENGTH * level
    for line in diff:
        key = line['key']
        status = line['status']
        value = stylish_stringify(line['value'], level + 1)
        old_value = stylish_stringify(line.get('old_value'), level + 1)
        indent = (
            indent_length * INDENT_UNIT
            if status in ("nested", "unchanged")
            else (indent_length - PREFIX_LENGTH) * INDENT_UNIT
        )
        if status == 'added':
            text_lines.append(
                f"{indent}{PREFIX['added']}{key}: {value}"
                )
        elif status == 'removed':
            text_lines.append(
                f"{indent}{PREFIX['removed']}{key}: {value}"
                )
        elif status == 'unchanged':
            text_lines.append(f"{indent}{key}: {value}")
        elif status == 'nested':
            text_lines.append(
                f"{indent}{key}: {format_stylish(line['value'], level + 1)}"
            )
        elif status == 'updated':
            text_lines.append(
                f"{indent}{PREFIX['removed']}{key}: {old_value}"
                )
            text_lines.append(
                f"{indent}{PREFIX['added']}{key}: {value}"
                )
    bracket_indent = LEVEL_LENGTH * (level - 1) * INDENT_UNIT
    return f"{{\n{'\n'.join(text_lines)}\n{bracket_indent}}}"


def format_diff(diff: list[dict[str, Any]], format_name: str) -> str:
    if format_name == 'stylish':
        return format_stylish(diff)
