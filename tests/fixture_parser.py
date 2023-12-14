from json import load


def parse_txt(file_path):
    with open(file_path) as file:
        return file.read().strip()


def parse_json(file_path):
    with open(file_path) as file:
        return load(file)
