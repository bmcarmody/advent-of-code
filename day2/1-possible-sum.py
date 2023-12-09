import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

bag_contents = {'red': 12, 'green': 13, 'blue': 14}
runningTotal = 0

with open('./input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        lineIndex = line.split(':')[0].split(' ')[1]
        lineContent = line.split(':')[1]

        gameList = lineContent.split(';')
        isPossible = True

        for game in gameList:
            game = game.strip()
            game = game.split(',')

            for cube in game:
                cube = cube.strip()
                cube = cube.split(' ')

                if int(cube[0]) > bag_contents[cube[1]]:
                    isPossible = False
                    break

        if isPossible:
            runningTotal += int(lineIndex)

logging.info(runningTotal)
