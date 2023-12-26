DEFAULT_VALUE = "nonexistent"


def get_diff(dict1, dict2):
    diff = []
    keys = sorted(list(set(dict1) | set(dict2)))

    for key in keys:
        value1 = dict1.get(key, DEFAULT_VALUE)
        value2 = dict2.get(key, DEFAULT_VALUE)

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({"key": key, "nested": get_diff(value1, value2)})
        else:
            diff.append({
                "key": key,
                "old value": value1,
                "new value": value2,
            })

    return diff
