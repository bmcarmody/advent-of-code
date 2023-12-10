import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

totalPoints = 0

with open('./input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        lineScore = 0

        lineContent = line.split(':')[1].strip()
        winningNumbers, myNumbers = lineContent.split(' | ')

        winningNumbersList = winningNumbers.strip().split(' ')
        myNumbersList = myNumbers.strip().split(' ')

        for myNumber in myNumbersList:
            if myNumber == '':
                continue
            if myNumber in winningNumbersList:
                if lineScore == 0:
                    lineScore = 1
                else:
                    lineScore *= 2

        totalPoints += lineScore

logging.info(totalPoints)
