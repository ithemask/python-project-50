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


def get_plain_view(path, action, value):
    beginning = f"Property '{path}' was"
    if action == 'ADDED':
        return f'{beginning} added with value: {format_(value)}'
    if action == 'REMOVED':
        return f'{beginning} removed'
    if action == 'CHANGED':
        old_value, new_value = value
        return (
            f'{beginning} updated. '
            f'From {format_(old_value)} to {format_(new_value)}'
        )


def plainify(diff):

    def walk(diff, path, output):
        for entry in diff:
            key = entry['key']
            action = entry['action']
            value = entry['value']

            if action == 'UNCHANGED':
                continue
            if action == 'NESTED':
                walk(value, path + [key], output)
            else:
                output.append(get_plain_view(
                    '.'.join(path + [key]),
                    action,
                    value,
                ))
        return output

    return '\n'.join(walk(diff, [], []))
