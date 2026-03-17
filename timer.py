import time
import datetime
import subprocess
from pathlib import Path
from settings import getSettings

settings = getSettings()
print(settings)

while True:
    a = subprocess.run(['gnome-screensaver-command', '-q'], capture_output=True,
text=True).stdout
    dateTime = datetime.datetime.now().isoformat()
    date = dateTime[:10]
    print(dateTime)
    print(date)
    activityFile = f'activity_{settings["machineName"]}_{date}.txt'
    activityPathFile = Path(settings['activityDirectory']) / activityFile
    if 'The screensaver is inactive' in a:
        with open(activityPathFile, 'a') as f:
            f.write(f'{dateTime},active\n')
    else:
        with open(activityPathFile, 'a') as f:
            f.write(f'{dateTime},inactive\n')
    time.sleep(60)

