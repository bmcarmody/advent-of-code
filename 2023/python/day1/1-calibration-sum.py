runningTotal = 0

with open('./input.txt', 'r') as file:
    for line in file:
        line = line.strip()

        left = 0
        right = len(line) - 1

        while left <= right:
            if not line[left].isdigit():
                left += 1

            if not line[right].isdigit():
                right -= 1

            if line[left].isdigit() and line[right].isdigit():
                break

        concatLeftRight = str(line[left]) + str(line[right])
        runningTotal += int(concatLeftRight)

print(runningTotal)
