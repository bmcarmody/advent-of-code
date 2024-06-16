package main

import (
	"bmcarmody-aoc-2022/utils"
	"fmt"
	"strings"
)

var dataFilePath = "input.txt"
var charToPriority [128]int

func part1() {
	var prioritySum int = 0

	parseLine := func(line string) {
		strings.TrimSpace(line)
		itemLength := len(line) / 2
		item1, item2 := line[:itemLength], line[itemLength:]

		charMap := make(map[rune]bool)
		var overlappingChar rune

		for _, char := range item1 {
			charMap[char] = true
		}

		for _, char := range item2 {
			if charMap[char] {
				overlappingChar = char

				break
			}
		}

		prioritySum += charToPriority[overlappingChar]
	}

	utils.ReadFile(dataFilePath, parseLine)

	fmt.Printf("Priority Sum: %d", prioritySum)
}

func main() {
	for i := 0; i < 26; i++ {
		charToPriority['a'+i] = i + 1
		charToPriority['A'+i] = i + 27
	}

	part1()
}
