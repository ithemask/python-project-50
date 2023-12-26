from gendiff.diff import DEFAULT_VALUE
from gendiff.formatters.value_formatter import format_more


def get_plain_view(path, old_value, new_value):
    beginning = f"Property '{path}' was "
    if new_value == DEFAULT_VALUE:
        return beginning + "removed"
    if old_value == DEFAULT_VALUE:
        return beginning + f"added with value: {format_more(new_value)}"
    else:
        return (
            beginning
            + "updated. "
            + f"From {format_more(old_value)} to {format_more(new_value)}"
        )


def plained(diff):

    def walk(diff, path, output):
        for entry in diff:
            key = entry["key"]
            nested = entry.get("nested")
            if nested:
                walk(nested, path + [key], output)
            else:
                old_value = entry["old value"]
                new_value = entry["new value"]
                if old_value == new_value:
                    continue
                output.append(get_plain_view(
                    ".".join(path + [key]),
                    old_value,
                    new_value,
                ))
        return output

    return "\n".join(walk(diff, [], []))
