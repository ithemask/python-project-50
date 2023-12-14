from gendiff.diff import get_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def generate_diff(file_path1, file_path2, output_format="stylish"):
    if output_format == "stylish":
        apply_format = stylish
    elif output_format == "plain":
        apply_format = plain
    else:
        raise ValueError(
            f'Invalid output format "{output_format}". ' +
            'Available formats are: "stylish", "plain".'
        )
    return apply_format(get_diff(file_path1, file_path2))
