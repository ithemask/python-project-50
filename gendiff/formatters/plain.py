def format_(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{str(value)}'"
    if value is None:
        return 'null'
    return str(value)


def get_plain_view(path, action, old_value, new_value):
    beginning = f"Property '{path}' was "
    if action == 'ADDED':
        return beginning + f'added with value: {format_(new_value)}'
    if action == 'REMOVED':
        return beginning + 'removed'
    if action == 'CHANGED':
        return (
            beginning
            + 'updated. '
            + f'From {format_(old_value)} to {format_(new_value)}'
        )


def plainify(diff):

    def walk(diff, path, output):
        for entry in diff:
            key = entry['key']
            nested = entry.get('nested')
            if nested:
                walk(nested, path + [key], output)
            else:
                action = entry['action']
                old_value = entry['old value']
                new_value = entry['new value']
                if action == 'UNCHANGED':
                    continue
                output.append(get_plain_view(
                    '.'.join(path + [key]),
                    action,
                    old_value,
                    new_value,
                ))
        return output

    return '\n'.join(walk(diff, [], []))
