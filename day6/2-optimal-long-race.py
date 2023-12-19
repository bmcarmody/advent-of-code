import math

input = {
    'time': [58, 81, 96, 76],
    'distance': [434, 1041, 2219, 1218]
}

raceTime = int(''.join(str(i) for i in input['time']))
raceDistance = int(''.join(str(i) for i in input['distance']))

fastestSpeed = raceTime
timeToFinishAtFastestSpeed = raceDistance / fastestSpeed
latestTimeToStart = math.ceil(raceTime - timeToFinishAtFastestSpeed)

timesToStartThatFinish = []
for k in range(latestTimeToStart, 0, -1):
    currentSpeed = k
    timeRemaining = raceTime - k
    timeToFinishAtCurrentSpeed = raceDistance / currentSpeed

    if (timeRemaining - timeToFinishAtCurrentSpeed) <= 0:
        continue

    timesToStartThatFinish.append(k)

print(len(timesToStartThatFinish))
