import json

def load_scenario(path):
    with open(path, "r") as file:
        return json.load(file)
    