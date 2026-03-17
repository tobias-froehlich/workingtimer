import os
import json

if os.path.exists('settings.json'):
    raise Exception('File settings.json already exists.')

settings = {
    'activityDirectory': '',
    'machineName': '',
    'allMachineNames': [],
}

with open('settings.json', 'w') as f:
    f.write(json.dumps(settings, indent=4))

