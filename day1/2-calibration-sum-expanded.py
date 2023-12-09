import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

runningTotal = 0
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number_dict = {word: index + 1 for index, word in enumerate(numbers)}

with open('./input.txt', 'r') as file:
    for line in file:
        line = line.strip()

        leftIndex = 0
        leftNumber = 0
        rightIndex = len(line) - 1
        rightNumber = 0

        while leftIndex <= rightIndex:
            if not line[leftIndex].isdigit():
                leftIndex += 1

            if not line[rightIndex].isdigit():
                rightIndex -= 1

            if line[leftIndex].isdigit() and line[rightIndex].isdigit():
                leftNumber = int(line[leftIndex])
                rightNumber = int(line[rightIndex])
                break
            
        for num in numbers:
            firstIndex = line.find(num)
            lastIndex = line.rfind(num)
            
            if firstIndex != -1 and firstIndex < leftIndex:
                leftIndex = firstIndex
                leftNumber = number_dict[num]
            if lastIndex != -1 and lastIndex > rightIndex:
                rightIndex = lastIndex
                rightNumber = number_dict[num]
            
        concatLeftRight = str(leftNumber) + str(rightNumber)
        runningTotal += int(concatLeftRight)

logging.info(runningTotal)
