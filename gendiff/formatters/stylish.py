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


def form_string(key, action, value, depth, indent):
    if action == 'CHANGED':
        old_value, new_value = value
        return '\n'.join((
            get_stylish_view(key, old_value, '- ', depth, indent),
            get_stylish_view(key, new_value, '+ ', depth, indent),
        ))
    match action:
        case 'ADDED':
            special_char = '+ '
        case 'REMOVED':
            special_char = '- '
        case 'UNCHANGED':
            special_char = '  '
    return get_stylish_view(key, value, special_char, depth, indent)


def stylishify(diff):

    def walk(diff, output, depth):
        indent = (INDENT_CHARS * depth)[0:OFFSET]
        for entry in diff:
            key = entry['key']
            action = entry['action']
            value = entry['value']

            if action == 'NESTED':
                output.append(f'{indent}  {key}: {{')
                walk(value, output, depth + 1)
                output.append(f'{INDENT_CHARS * depth}}}')
            else:
                output.append(form_string(
                    key,
                    action,
                    value,
                    depth,
                    indent,
                ))

        return output

    lines = '\n'.join(walk(diff, [], 1))
    return f'{{\n{lines}\n}}'
