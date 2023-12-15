from gendiff.diff import get_diff
from gendiff.formatters.stylish import stylished
from gendiff.formatters.plain import plained


def generate_diff(file_path1, file_path2, output_format="stylish"):
    if output_format == "stylish":
        apply_format = stylished
    elif output_format == "plain":
        apply_format = plained
    else:
        raise ValueError(
            f'Invalid output format "{output_format}". ' +
            'Available formats are: "stylish", "plain".'
        )
    return apply_format(get_diff(file_path1, file_path2))
