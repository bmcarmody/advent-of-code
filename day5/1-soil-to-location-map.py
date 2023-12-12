seedToLocationDict = {}

mapDict = {
    'seed-to-soil map:': [],
    'soil-to-fertilizer map:': [],
    'fertilizer-to-water map:': [],
    'water-to-light map:': [],
    'light-to-temperature map:': [],
    'temperature-to-humidity map:': [],
    'humidity-to-location map:': [],
}


with open('./input.txt', 'r') as file:
    currentList = None
    for lineIndex, line in enumerate(file):
        line = line.strip()

        if line == '':
            continue

        if lineIndex == 0:
            stringSeedList = line.split(':')[1].strip().split(' ')
            seedToLocationDict = {int(i): None for i in stringSeedList}
            continue

        if line in mapDict.keys():
            currentList = mapDict[line]
            continue

        stringLineList = line.strip().split(' ')
        intLineList = [int(i) for i in stringLineList]
        currentList.append(intLineList)


def getDestination(currentValue, currentMap):
    destination = currentValue
    for newDestination, source, rangeToSpan in currentMap:
        if currentValue >= source and currentValue <= source + rangeToSpan:
            destination = currentValue - source + newDestination
            break

    return destination


for seed in seedToLocationDict.keys():
    destination = seed
    for currentMap in mapDict.values():
        destination = getDestination(destination, currentMap)
    seedToLocationDict[seed] = destination

print(min(seedToLocationDict.values()))
