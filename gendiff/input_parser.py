from json import loads as json_load
from yaml import full_load as yaml_load


def read_input(file_path):
    with open(file_path) as file:
        input_ = file.read()
        return input_


def parse_input(file_path):
    input_ = read_input(file_path)
    _, extension = file_path.split('.')
    if extension == 'json':
        return json_load(input_)
    if extension in ('yml', 'yaml'):
        return yaml_load(input_)
    else:
        raise TypeError(
            f'Invalid file type .{extension}. '
            + 'Available types are: .json, .yml, .yaml.'
        )
