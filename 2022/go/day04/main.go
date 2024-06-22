package main

import (
	"bmcarmody-aoc-2022/utils"
	"fmt"
	"strconv"
	"strings"
)

var dataFilePath = "input.txt"

func part1() {
	var fullyContainedCounter = 0

	parseLine := func(line string) {
		strings.TrimSpace(line)
		parts := strings.Split(line, ",")
		range1, range2 := parts[0], parts[1]

		range1Parts := strings.Split(range1, "-")
		range2Parts := strings.Split(range2, "-")

		range1Start, range1StartErr := strconv.Atoi(range1Parts[0])
		utils.CheckError("Error converting range1Start to int", range1StartErr)
		range1End, range1EndErr := strconv.Atoi(range1Parts[1])
		utils.CheckError("Error converting range1End to int", range1EndErr)

		range2Start, range2StartErr := strconv.Atoi(range2Parts[0])
		utils.CheckError("Error converting range2Start to int", range2StartErr)
		range2End, range2EndErr := strconv.Atoi(range2Parts[1])
		utils.CheckError("Error converting range2End to int", range2EndErr)

		largestStart := utils.MaxInt(range1Start, range2Start)
		largestEnd := utils.MaxInt(range1End, range2End)

		if ((range1Start != largestStart) && (range1End != largestEnd)) || (range2Start != largestStart) && (range2End != largestEnd) {
			return
		}

		fullyContainedCounter += 1
	}

	utils.ReadFile(dataFilePath, parseLine)
	fmt.Printf("Fully Contained Pairs: %d", fullyContainedCounter)
}

func part2() {
	var partiallyContainedCounter = 0

	parseLine := func(line string) {
		strings.TrimSpace(line)
		parts := strings.Split(line, ",")
		range1, range2 := parts[0], parts[1]

		range1Parts := strings.Split(range1, "-")
		range2Parts := strings.Split(range2, "-")

		range1Start, range1StartErr := strconv.Atoi(range1Parts[0])
		utils.CheckError("Error converting range1Start to int", range1StartErr)
		range1End, range1EndErr := strconv.Atoi(range1Parts[1])
		utils.CheckError("Error converting range1End to int", range1EndErr)

		range2Start, range2StartErr := strconv.Atoi(range2Parts[0])
		utils.CheckError("Error converting range2Start to int", range2StartErr)
		range2End, range2EndErr := strconv.Atoi(range2Parts[1])
		utils.CheckError("Error converting range2End to int", range2EndErr)

		if (range1Start <= range2Start || range2End >= range1Start) && (range2Start <= range1End || range2End <= range1End) {
			fmt.Printf("Matched %s\n", line)
			partiallyContainedCounter += 1

			return
		}

		fmt.Printf("Skipped Matched %s\n", line)
	}

	utils.ReadFile(dataFilePath, parseLine)
	fmt.Printf("Partially Contained Pairs: %d", partiallyContainedCounter)
}

func main() {
	part1()
	part2()
}
