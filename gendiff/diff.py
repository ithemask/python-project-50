DEFAULT_VALUE = "nonexistent"


def get_action(old_value, new_value):
    if old_value == DEFAULT_VALUE:
        return 'ADDED'
    if new_value == DEFAULT_VALUE:
        return 'REMOVED'
    if old_value != new_value:
        return 'CHANGED'
    return 'UNCHANGED'


def get_diff(dict1, dict2):
    diff = []
    keys = sorted(list(set(dict1) | set(dict2)))

    for key in keys:
        old_value = dict1.get(key, DEFAULT_VALUE)
        new_value = dict2.get(key, DEFAULT_VALUE)

        if isinstance(old_value, dict) and isinstance(new_value, dict):
            diff.append({"key": key, "nested": get_diff(old_value, new_value)})
        else:
            diff.append({
                "key": key,
                "action": get_action(old_value, new_value),
                "old value": old_value,
                "new value": new_value,
            })

    return diff
