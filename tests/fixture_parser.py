def parse_txt(file_path):
    with open(file_path) as file:
        return file.read().strip()
