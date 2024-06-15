package main

import (
	"bmcarmody-aoc-2022/utils"
	"fmt"
	"sort"
	"strconv"
)

var dataFilePath = "input.txt"

func part1() {
	maxCalories := 0
	currentCaloriesTotal := 0

	getMaxCalories := func(line string) {
		if line == "" {
			currentCaloriesTotal = 0
			return
		}

		caloriesInt, err := strconv.Atoi(line)
		utils.CheckError("Error converting line to integer:", err)

		currentCaloriesTotal += caloriesInt

		if currentCaloriesTotal > maxCalories {
			maxCalories = currentCaloriesTotal
		}
	}

	utils.ReadFile(dataFilePath, getMaxCalories)
	fmt.Printf("Max calories: %d\n", maxCalories)
}

func part2() {
	var caloriesPerElf []int
	currentCaloriesTotal := 0

	calculateCaloriesPerElf := func(line string) {
		if line == "" {
			caloriesPerElf = append(caloriesPerElf, currentCaloriesTotal)
			currentCaloriesTotal = 0
			return
		}

		caloriesInt, err := strconv.Atoi(line)
		utils.CheckError("Error converting line to integer:", err)

		currentCaloriesTotal += caloriesInt
	}

	utils.ReadFile(dataFilePath, calculateCaloriesPerElf)
	sort.Ints(caloriesPerElf)
	topThreeMaxCalories := caloriesPerElf[len(caloriesPerElf)-3:]
	topThreeMaxCaloriesTotal := 0

	for _, calories := range topThreeMaxCalories {
		topThreeMaxCaloriesTotal += calories
	}

	fmt.Printf("Top three max calories: %d\n", topThreeMaxCaloriesTotal)
}

func main() {
	part1()
	part2()
}
