import math

input = {
    'time': [58, 81, 96, 76],
    'distance': [434, 1041, 2219, 1218]
}

runningTotal = 1
for i in range(4):
    raceTime = input['time'][i]
    raceDistance = input['distance'][i]

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
    runningTotal *= len(timesToStartThatFinish)

print(runningTotal)
