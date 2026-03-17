import datetime
import sys
import os
from pathlib import Path
from settings import getSettings

settings = getSettings()


errorString = "Give exactly one argument in the form 'yyyy-mm'"
assert len(sys.argv) == 2, errorString
assert len(sys.argv[1].split('-')) == 2, errorString
assert len(sys.argv[1].split('-')[0]) == 4, errorString
assert len(sys.argv[1].split('-')[1]) == 2, errorString
assert sys.argv[1].split('-')[0].isdigit(), errorString
assert sys.argv[1].split('-')[1].isdigit(), errorString
assert 1 <= int(sys.argv[1].split('-')[1]) <= 12, errorString

def getTimeForDateAndMachine(date, machineName):    
    
    activityFilename = Path(settings['activityDirectory']) / f'activity_{machineName}_{date}.txt'
    linesToday = []
    try:
        with open(activityFilename, 'r') as f:
            for line in f:
                if line.startswith(date):
                    linesToday.append(line.replace('\n', ''))
    except:
        return datetime.timedelta(0)
    
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
    
    return timeActive

def getTimeForDate(date):
    timeActive = datetime.timedelta(0)
    for machineName in settings['allMachineNames']:
        timeActive += getTimeForDateAndMachine(date, machineName)
    return timeActive

dates = []
for i in range(1, 32):
    dateString = f'{sys.argv[1]}-{i:02d}'
    try:
        date = datetime.datetime.fromisoformat(dateString)
        dates.append(dateString)
    except:
        pass


def getWeekday(date):
    return datetime.datetime.fromisoformat(date).strftime('%A')


filename = Path(settings['outputDirectoryForMonth']) / f'{sys.argv[1]}.txt'
if not os.path.isfile(filename):
    print('generating file')
    with open(filename, 'w') as f:
        for date in dates:
            f.write(f'{date} {getWeekday(date):9s} \n')

writtenTimes = {}
with open(filename, 'r') as f:
    for line in f:
        words = line.split()
        assert len(words) in [2, 3], 'The lines must have 2 or 3 words.'

        if len(words) == 2:
            activeTime = 0
        else:
            activeTime = int(words[2])
        writtenTimes[words[0]] = activeTime

print(writtenTimes)

notYetWritten = 0
workHours = 0
for date in dates:
    timeForDate = getTimeForDate(date)
    deltaMinutes = timeForDate.seconds / 60 - writtenTimes[date] * 60
    workHours += writtenTimes[date]
    notYetWritten += deltaMinutes
    print(f'{date} {getWeekday(date):9s} {timeForDate} {deltaMinutes:.0f}')

print(f'You have written down {workHours / 8:.2f} days, which are {workHours} hours.')
print(f'You have {notYetWritten:.0f} minutes not written down.')

