from json import dumps


def get_jsoned(diff):
    return dumps(diff, indent=2)
