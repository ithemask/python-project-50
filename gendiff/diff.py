from gendiff.input_parser import parse_input


DEFAULT_VALUE = "nonexistent"


def get_diff(file_path1, file_path2):
    config1 = parse_input(file_path1)
    config2 = parse_input(file_path2)

    def walk(dict1, dict2):
        diff = []
        keys = sorted(list(set(dict1) | set(dict2)))

        for key in keys:
            value1 = dict1.get(key, DEFAULT_VALUE)
            value2 = dict2.get(key, DEFAULT_VALUE)

            if isinstance(value1, dict) and isinstance(value2, dict):
                diff.append({"key": key, "nested": walk(value1, value2)})
            else:
                diff.append({
                    "key": key,
                    "old value": value1,
                    "new value": value2,
                })

        return diff

    return walk(config1, config2)
