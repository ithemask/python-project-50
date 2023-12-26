from json import load as json_load
from yaml import full_load as yaml_load


def parse_input(file_path):
    with open(file_path) as file:
        _, extension = file_path.split('.')
        if extension == 'json':
            return json_load(file)
        if extension in ('yml', 'yaml'):
            return yaml_load(file)
        else:
            raise TypeError(
                f'Invalid file type .{extension}. '
                + 'Available types are: .json, .yml, .yaml.'
            )
