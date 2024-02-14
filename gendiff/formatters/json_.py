from json import dumps


def jsonify(diff):
    return dumps(diff, indent=2)
