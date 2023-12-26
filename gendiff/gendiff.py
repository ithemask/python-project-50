from gendiff.input_parser import parse_input
from gendiff.diff import get_diff
from gendiff.formatters.stylish import stylished
from gendiff.formatters.plain import plained
from gendiff.formatters.json_ import jsoned


def generate_diff(file_path1, file_path2, output_format="stylish"):
    config1 = parse_input(file_path1)
    config2 = parse_input(file_path2)

    if output_format == "stylish":
        apply_format = stylished
    elif output_format == "plain":
        apply_format = plained
    elif output_format == "json":
        apply_format = jsoned
    else:
        raise ValueError(
            f'Invalid output format "{output_format}". '
            + 'Available formats are: "stylish", "plain", "json".'
        )

    return apply_format(get_diff(config1, config2))
