from gendiff.input_parser import parse_input


DEFAULT_VALUE = "impossible_value"


def format_(value):
    return str(value).lower() if value in (True, False, None) else value


def update_output(output, prefix, key, value):
    output.append(f"  {prefix} {key}: {format_(value)}")


def generate_diff(file_path1, file_path2):
    output = []
    config1 = parse_input(file_path1)
    config2 = parse_input(file_path2)
    keys = sorted(list(set(config1) | set(config2)))

    for key in keys:
        value1 = config1.get(key, DEFAULT_VALUE)
        value2 = config2.get(key, DEFAULT_VALUE)
        if value1 == value2:
            update_output(output, " ", key, value1)
        elif DEFAULT_VALUE not in (value1, value2):
            update_output(output, "-", key, value1)
            update_output(output, "+", key, value2)
        elif value2 == DEFAULT_VALUE:
            update_output(output, "-", key, value1)
        else:
            update_output(output, "+", key, value2)

    return "{\n" + "\n".join(output) + "\n}"