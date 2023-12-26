from gendiff.diff import DEFAULT_VALUE
from gendiff.formatters.value_formatter import format_


INDENT_CHARS = "    "
OFFSET = -2


def get_stylish_view(key, value, special_char, depth, indent):

    def walk(dict_, output, depth, indent):
        for key, value in dict_.items():
            beginning = f"{INDENT_CHARS * depth + key}: "
            if isinstance(value, dict):
                output.append(
                    beginning
                    + walk(value, [], depth + 1, indent + INDENT_CHARS)
                )
            else:
                output.append(beginning + format_(value))
        return (
            "{\n" + "\n".join(output)
            + f"\n{indent + INDENT_CHARS[0:OFFSET]}" + "}"
        )

    if isinstance(value, dict):
        formatted = walk(value, [], depth + 1, indent)
    else:
        formatted = format_(value)
    return f"{indent + special_char + key}: {formatted}"


def form_string(key, old_value, new_value, depth, indent):
    if old_value == new_value:
        return get_stylish_view(key, old_value, "  ", depth, indent)
    if DEFAULT_VALUE not in (old_value, new_value):
        return "\n".join((
            get_stylish_view(key, old_value, "- ", depth, indent),
            get_stylish_view(key, new_value, "+ ", depth, indent),
        ))
    if DEFAULT_VALUE == new_value:
        return get_stylish_view(key, old_value, "- ", depth, indent)
    if DEFAULT_VALUE == old_value:
        return get_stylish_view(key, new_value, "+ ", depth, indent)


def stylished(diff):

    def walk(diff, output, depth):
        indent = (INDENT_CHARS * depth)[0:OFFSET]
        for entry in diff:
            key = entry["key"]
            nested = entry.get("nested")
            special_char = "  "
            if nested:
                output.append(indent + special_char + key + ": {")
                walk(nested, output, depth + 1)
                output.append(indent + INDENT_CHARS[0:OFFSET] + "}")
            else:
                old_value = entry["old value"]
                new_value = entry["new value"]
                output.append(
                    form_string(key, old_value, new_value, depth, indent)
                )
        return output

    return "{\n" + "\n".join(walk(diff, [], 1)) + "\n}"
