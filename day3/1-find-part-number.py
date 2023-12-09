import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
inputLineList = []

totalSum = 0


def isCharSpecialCharacter(char):
    return char != '.' and not char.isdigit()


with open('./input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        charLineList = []
        for char in line:
            charLineList.append(char)
        inputLineList.append(charLineList)

for charLineListIndex, charLineList in enumerate(inputLineList):
    runningDigit = ''
    isPartNumber = False
    for charIndex, char in enumerate(charLineList):
        if char == '.' or not char.isdigit():
            runningDigit = ''
            isPartNumber = False
            continue

        runningDigit += char
        isFirstChar = charIndex == 0
        isLastChar = charIndex == len(charLineList) - 1
        if isPartNumber:
            if isLastChar or not charLineList[charIndex + 1].isdigit():
                totalSum += int(runningDigit)
                runningDigit = ''
            continue
        surroundingChars = []
        # Check behind
        if not isFirstChar:
            surroundingChars.append(charLineList[charIndex - 1])
        # Check ahead
        if not isLastChar:
            surroundingChars.append(charLineList[charIndex + 1])
        # Ckeck above
        if charLineListIndex != 0:
            surroundingChars.append(
                inputLineList[charLineListIndex - 1][charIndex])
            if not isFirstChar:
                surroundingChars.append(
                    inputLineList[charLineListIndex - 1][charIndex - 1])
            if not isLastChar:
                surroundingChars.append(
                    inputLineList[charLineListIndex - 1][charIndex + 1])
        # Check below
        if charLineListIndex != len(inputLineList) - 1:
            surroundingChars.append(
                inputLineList[charLineListIndex + 1][charIndex])
            if not isFirstChar:
                surroundingChars.append(
                    inputLineList[charLineListIndex + 1][charIndex - 1])
            if not isLastChar:
                surroundingChars.append(
                    inputLineList[charLineListIndex + 1][charIndex + 1])

        hasSpecialChar = any(isCharSpecialCharacter(
            surroundingChar) for surroundingChar in surroundingChars)
        if hasSpecialChar:
            isPartNumber = True
            if isLastChar or not charLineList[charIndex + 1].isdigit():
                totalSum += int(runningDigit)
                runningDigit = ''

logging.info(totalSum)
