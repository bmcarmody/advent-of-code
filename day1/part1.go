package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strconv"
)

func main() {
	currentDir, err := os.Getwd()
	if err != nil {
		log.Fatalf("Error getting current directory: %s", err)
	}

	filePath := filepath.Join(currentDir, "day1", "part1.txt")
	file, err := os.Open(filePath)

	if err != nil {
		log.Fatalf("Error opening file: %s", err)
		return
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	maxCalories := 0
	currentCaloriesTotal := 0

	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			currentCaloriesTotal = 0
			continue
		}

		caloriesInt, err := strconv.Atoi(line)
		if err != nil {
			log.Fatalf("Error converting line to integer: %s", err)
		}

		currentCaloriesTotal += caloriesInt

		if currentCaloriesTotal > maxCalories {
			maxCalories = currentCaloriesTotal
		}
	}

	fmt.Printf("Max calories: %d\n", maxCalories)

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error scanning file: %s", err)
	}
}
