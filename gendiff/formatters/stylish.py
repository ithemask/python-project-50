INDENT_CHARS = '    '
OFFSET = -2


def format_(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def get_stylish_view(key, value, special_char, depth, indent):

    def walk(dict_, output, depth):
        for key, value in dict_.items():
            beginning = f'{INDENT_CHARS * depth}{key}:'
            if isinstance(value, dict):
                output.append(f'{beginning} {walk(value, [], depth + 1)}')
            else:
                output.append(f'{beginning} {format_(value)}')
        lines = '\n'.join(output)
        return f'{{\n{lines}\n{INDENT_CHARS * (depth - 1)}}}'

    if isinstance(value, dict):
        formatted = walk(value, [], depth + 1)
    else:
        formatted = format_(value)

    return f'{indent}{special_char}{key}: {formatted}'


def form_string(key, action, old_value, new_value, depth, indent):
    if action == 'ADDED':
        return get_stylish_view(key, new_value, '+ ', depth, indent)
    if action == 'REMOVED':
        return get_stylish_view(key, old_value, '- ', depth, indent)
    if action == 'CHANGED':
        return '\n'.join((
            get_stylish_view(key, old_value, '- ', depth, indent),
            get_stylish_view(key, new_value, '+ ', depth, indent),
        ))
    if action == 'UNCHANGED':
        return get_stylish_view(key, old_value, '  ', depth, indent)


def stylishify(diff):

    def walk(diff, output, depth):
        indent = (INDENT_CHARS * depth)[0:OFFSET]
        for entry in diff:
            key = entry['key']
            nested = entry.get('nested')
            special_char = '  '
            if nested:
                output.append(f'{indent}{special_char}{key}: {{')
                walk(nested, output, depth + 1)
                output.append(f'{INDENT_CHARS * depth}}}')
            else:
                action = entry['action']
                old_value = entry['old value']
                new_value = entry['new value']
                output.append(form_string(
                    key,
                    action,
                    old_value,
                    new_value,
                    depth,
                    indent,
                ))
        return output

    lines = '\n'.join(walk(diff, [], 1))
    return f'{{\n{lines}\n}}'
