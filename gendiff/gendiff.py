from gendiff.input_parser import parse_input
from gendiff.diff import get_diff
from gendiff.formatters.stylish import stylishify
from gendiff.formatters.plain import plainify
from gendiff.formatters.json_ import jsonify


def generate_diff(file_path1, file_path2, output_format='stylish'):
    config1 = parse_input(file_path1)
    config2 = parse_input(file_path2)

    if output_format == 'stylish':
        apply_format = stylishify
    elif output_format == 'plain':
        apply_format = plainify
    elif output_format == 'json':
        apply_format = jsonify
    else:
        raise ValueError(
            f'Invalid output format "{output_format}". '
            + 'Available formats are: "stylish", "plain", "json".'
        )

    return apply_format(get_diff(config1, config2))
