from json import load as json_load
from yaml import full_load as yaml_load


def parse_input(file_path):
    with open(file_path) as file:
        if file_path.endswith(".json"):
            return json_load(file)
        return yaml_load(file)
