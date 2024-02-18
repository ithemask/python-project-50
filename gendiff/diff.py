def get_action_and_value(key_in_dict1, key_in_dict2, old_value, new_value):
    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return 'NESTED', get_diff(old_value, new_value)
    if key_in_dict2 and not key_in_dict1:
        return 'ADDED', new_value
    if key_in_dict1 and not key_in_dict2:
        return 'REMOVED', old_value
    if old_value != new_value:
        return 'CHANGED', (old_value, new_value)
    return 'UNCHANGED', old_value


def get_diff(dict1, dict2):
    diff = []
    keys = sorted(list(set(dict1) | set(dict2)))

    for key in keys:
        old_value = dict1.get(key)
        new_value = dict2.get(key)
        action_and_value = get_action_and_value(
            key in dict1,
            key in dict2,
            old_value,
            new_value
        )
        diff.append({
            'key': key,
            'action': action_and_value[0],
            'value': action_and_value[1],
        })

    return diff
