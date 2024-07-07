import json

def load_into(filename, dest=None):
    if dest is None:
        dest = {}
    with open(filename, "a") as f:
        loaded_json = json.loads(f.read())
        dest.update(loaded_json)
    return dest
