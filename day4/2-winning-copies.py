import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

totalCards = 199
totalPoints = 0
copyCardsDict = {i: 0 for i in range(totalCards)}

with open('./input.txt', 'r') as file:
    for cardIndex, line in enumerate(file):
        line = line.strip()
        extraCardsWon = 0
        cardPoints = 0

        lineContent = line.split(':')[1].strip()
        winningNumbers, myNumbers = lineContent.split(' | ')

        winningNumbersList = winningNumbers.strip().split(' ')
        myNumbersList = myNumbers.strip().split(' ')

        for myNumber in myNumbersList:
            if myNumber == '':
                continue
            if myNumber in winningNumbersList:
                extraCardsWon += 1

        if extraCardsWon == 0:
            continue

        copiesToGiveOut = copyCardsDict[cardIndex]

        for i in range(copiesToGiveOut + 1):
            for j in range(extraCardsWon):
                currentCardIndex = cardIndex + j + 1
                # if copiesToGiveOut == 1:
                # logging.info(f'Giving out card {currentCardIndex + 1}')
                if currentCardIndex >= totalCards:
                    break

                copyCardsDict[currentCardIndex] += 1

totalPoints += totalCards
for value in copyCardsDict.values():
    totalPoints += value

logging.info(totalPoints)
