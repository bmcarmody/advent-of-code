mapDict = {
    'seed-to-soil map:': [],
    'soil-to-fertilizer map:': [],
    'fertilizer-to-water map:': [],
    'water-to-light map:': [],
    'light-to-temperature map:': [],
    'temperature-to-humidity map:': [],
    'humidity-to-location map:': [],
}
stringSeedList = []

with open('./input.txt', 'r') as file:
    currentList = None
    for lineIndex, line in enumerate(file):
        line = line.strip()

        if line == '':
            continue

        if lineIndex == 0:
            stringSeedList = line.split(':')[1].strip().split(' ')

            continue

        if line in mapDict.keys():
            currentList = mapDict[line]
            continue

        stringLineList = line.strip().split(' ')
        intLineList = [int(i) for i in stringLineList]
        currentList.append(intLineList)


def getSource(currentValue, currentMap):
    for newDestination, sourceStart, rangeToSpan in currentMap:
        if newDestination <= currentValue <= newDestination + rangeToSpan - 1:
            # Calculate the offset from the start of the destination range
            offset = currentValue - newDestination
            # Apply this offset to the source start
            return sourceStart + offset
    return currentValue


i = 0
breakFlag = False
while True:
    location = i
    for currentMap in reversed(list(mapDict.values())):
        location = getSource(location, currentMap)

    for seedIndex, seed in enumerate(stringSeedList):
        if seedIndex % 2 != 0:
            continue

        if location >= int(seed) and location < int(seed) + int(stringSeedList[seedIndex + 1]):
            breakFlag = True
            break

    if breakFlag:
        break

    i += 1

print(i)
