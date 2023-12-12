bag_contents = {'red': 12, 'green': 13, 'blue': 14}
runningTotal = 0

with open('./input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        lineIndex = line.split(':')[0].split(' ')[1]
        lineContent = line.split(':')[1]

        gameList = lineContent.split(';')
        minCubeList = {}

        for game in gameList:
            game = game.strip()
            game = game.split(',')

            for cube in game:
                cube = cube.strip()
                cube = cube.split(' ')

                if cube[1] not in minCubeList:
                    minCubeList[cube[1]] = int(cube[0])
                else:
                    if (int(cube[0])) > minCubeList[cube[1]]:
                        minCubeList[cube[1]] = int(cube[0])

        totalPower = 1
        for value in minCubeList.values():
            totalPower *= value

        runningTotal += totalPower

print(runningTotal)
