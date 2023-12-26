from gendiff.input_parser import parse_input
from gendiff.diff import get_diff
from gendiff.formatters.stylish import get_stylished
from gendiff.formatters.plain import get_plained
from gendiff.formatters.json_ import get_jsoned


def generate_diff(file_path1, file_path2, output_format="stylish"):
    config1 = parse_input(file_path1)
    config2 = parse_input(file_path2)

    if output_format == "stylish":
        apply_format = get_stylished
    elif output_format == "plain":
        apply_format = get_plained
    elif output_format == "json":
        apply_format = get_jsoned
    else:
        raise ValueError(
            f'Invalid output format "{output_format}". '
            + 'Available formats are: "stylish", "plain", "json".'
        )

    return apply_format(get_diff(config1, config2))
