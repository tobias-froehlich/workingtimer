import json

def getSettings():
    with open('settings.json', 'r') as f:
        content = f.read()
    return json.loads(content)
