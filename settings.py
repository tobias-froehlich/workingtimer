import json
import pathlib

def getSettings():
    with open(pathlib.Path(__file__).parent / 'settings.json', 'r') as f:
        content = f.read()
    return json.loads(content)
