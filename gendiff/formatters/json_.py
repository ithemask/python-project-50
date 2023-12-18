from json import dumps


def jsoned(diff):
    return dumps(diff, indent=2)
