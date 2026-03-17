import datetime
from pathlib import Path
from settings import getSettings

settings = getSettings()

print(settings)

today = datetime.datetime.now().isoformat().split('T')[0]

activityFilename = Path(settings['activityDirectory']) / f'activity_{settings["machineName"]}_{today}.txt'



print(today)


linesToday = []
with open(activityFilename, 'r') as f:
    for line in f:
        if line.startswith(today):
            linesToday.append(line.replace('\n', ''))

lines = []
for line in linesToday:
    words = line.split(',')
    lines.append((datetime.datetime.fromisoformat(words[0]), words[1]))

timeActive = datetime.timedelta(0)
timeInactive = datetime.timedelta(0)
for i in range(len(lines) - 1):
    time = (lines[i + 1][0] - lines[i][0])
    if time < datetime.timedelta(minutes=2):
        if lines[i][1] == 'active' and lines[i+1][1] == 'active':
            timeActive += time
    else:
        timeInactive += time

print(timeActive)
print(timeInactive)
