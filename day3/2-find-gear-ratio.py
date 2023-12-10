import logging
import functools
import operator

logging.basicConfig(level=logging.INFO, format='%(message)s')
inputLineList = []

totalSum = 0


def isCharSpecialCharacter(char):
    return char != '.' and not char.isdigit()


def findFullDigit(foundIndex, charLineList, isEnd=False, runningDigit=''):
    if not isEnd:
        if foundIndex != len(charLineList) - 1 and charLineList[foundIndex + 1].isdigit():
            return findFullDigit(foundIndex + 1, charLineList, False)
        return findFullDigit(foundIndex, charLineList, True)

    newRunningDigit = charLineList[foundIndex] + runningDigit
    if foundIndex != 0 and charLineList[foundIndex - 1].isdigit():
        return findFullDigit(foundIndex - 1, charLineList, True, newRunningDigit)
    return int(newRunningDigit)


with open('./input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        charLineList = []
        for char in line:
            charLineList.append(char)
        inputLineList.append(charLineList)

for charLineListIndex, charLineList in enumerate(inputLineList):

    for charIndex, char in enumerate(charLineList):
        if char != '*':
            continue

        isFirstChar = charIndex == 0
        isLastChar = charIndex == len(charLineList) - 1
        digits = []

        # Check behind
        if not isFirstChar:
            if charLineList[charIndex - 1].isdigit():
                fullDigit = findFullDigit(charIndex - 1, charLineList)
                digits.append(fullDigit)
        # Check ahead
        if not isLastChar:
            if charLineList[charIndex + 1].isdigit():
                fullDigit = findFullDigit(charIndex + 1, charLineList)
                digits.append(fullDigit)
        # Check above
        if charLineListIndex != 0:
            isAboveCharDigit = inputLineList[charLineListIndex -
                                             1][charIndex].isdigit()
            isAboveLeftCharDigit = inputLineList[charLineListIndex -
                                                 1][charIndex - 1].isdigit()
            isAboveRightCharDigit = inputLineList[charLineListIndex -
                                                  1][charIndex + 1].isdigit()

            if isAboveLeftCharDigit:
                fullDigit = findFullDigit(
                    charIndex - 1, inputLineList[charLineListIndex - 1])
                digits.append(fullDigit)

            if not isAboveLeftCharDigit and isAboveCharDigit:
                fullDigit = findFullDigit(
                    charIndex, inputLineList[charLineListIndex - 1])
                digits.append(fullDigit)

            if not isAboveCharDigit and isAboveRightCharDigit:
                fullDigit = findFullDigit(
                    charIndex + 1, inputLineList[charLineListIndex - 1])
                digits.append(fullDigit)

        # Check below
        if charLineListIndex != len(inputLineList) - 1:
            isBelowCharDigit = inputLineList[charLineListIndex +
                                             1][charIndex].isdigit()
            isBelowLeftCharDigit = inputLineList[charLineListIndex +
                                                 1][charIndex - 1].isdigit()
            isBelowRightCharDigit = inputLineList[charLineListIndex +
                                                  1][charIndex + 1].isdigit()

            if isBelowLeftCharDigit:
                fullDigit = findFullDigit(
                    charIndex - 1, inputLineList[charLineListIndex + 1])
                digits.append(fullDigit)

            if not isBelowLeftCharDigit and isBelowCharDigit:
                fullDigit = findFullDigit(
                    charIndex, inputLineList[charLineListIndex + 1])
                digits.append(fullDigit)

            if not isBelowCharDigit and isBelowRightCharDigit:
                fullDigit = findFullDigit(
                    charIndex + 1, inputLineList[charLineListIndex + 1])
                digits.append(fullDigit)

        if len(digits) != 2:
            continue

        logging.info(digits)

        totalSum += functools.reduce(operator.mul, digits)

logging.info(totalSum)
