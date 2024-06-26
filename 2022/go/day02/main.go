package main

import (
	"bmcarmody-aoc-2022/utils"
	"fmt"
	"strings"
)

var dataFilePath = "input.txt"

type TurnType string

const (
	Rock     TurnType = "Rock"
	Paper    TurnType = "Paper"
	Scissors TurnType = "Scissors"
)

type TurnResult string

const (
	Lost TurnResult = "Lost"
	Draw TurnResult = "Draw"
	Won  TurnResult = "Won"
)

var opponentGuideMap = map[string]TurnType{
	"A": TurnType(Rock),
	"B": TurnType(Paper),
	"C": TurnType(Scissors),
}

var personalGuideMap = map[string]TurnType{
	"X": TurnType(Rock),
	"Y": TurnType(Paper),
	"Z": TurnType(Scissors),
}

var turnTypeScoreMap = map[TurnType]int{
	TurnType(Rock):     1,
	TurnType(Paper):    2,
	TurnType(Scissors): 3,
}

var losingResultMap = map[TurnType]TurnType{
	TurnType(Rock):     TurnType(Paper),
	TurnType(Paper):    TurnType(Scissors),
	TurnType(Scissors): TurnType(Rock),
}

var turnResultScoreMap = map[TurnResult]int{
	TurnResult(Lost): 0,
	TurnResult(Draw): 3,
	TurnResult(Won):  6,
}

func part1() {
	totalScore := 0

	calculateScore := func(line string) {
		trimmedLine := strings.TrimSpace(line)
		parts := strings.Split(trimmedLine, " ")
		var opponentTurn TurnType = opponentGuideMap[parts[0]]
		var myTurn TurnType = personalGuideMap[parts[1]]
		myScore := turnTypeScoreMap[myTurn]
		var roundResult TurnResult

		switch {
		case opponentTurn == myTurn:
			roundResult = TurnResult(Draw)
		case losingResultMap[myTurn] == opponentTurn:
			roundResult = TurnResult(Lost)
		default:
			roundResult = TurnResult(Won)
		}

		roundScore := myScore + turnResultScoreMap[roundResult]
		totalScore += roundScore
	}

	utils.ReadFile(dataFilePath, calculateScore)

	fmt.Printf("Total Score: %d\n", totalScore)
}

var turnToResultMap = map[string]TurnResult{
	"X": TurnResult(Lost),
	"Y": TurnResult(Draw),
	"Z": TurnResult(Won),
}

// Just a reverse of losingResultMap
// Easier to create a new map than to implement
// value -> key logic considering how small the map is
var winningResultMap = map[TurnType]TurnType{
	TurnType(Rock):     TurnType(Scissors),
	TurnType(Paper):    TurnType(Rock),
	TurnType(Scissors): TurnType(Paper),
}

func part2() {
	totalScore := 0

	calculateScore := func(line string) {
		trimmedLine := strings.TrimSpace(line)
		parts := strings.Split(trimmedLine, " ")
		var opponentTurn TurnType = opponentGuideMap[parts[0]]
		myTurnResult := turnToResultMap[parts[1]]
		var myTurn TurnType

		switch myTurnResult {
		case Won:
			myTurn = losingResultMap[opponentTurn]
		case Lost:
			myTurn = winningResultMap[opponentTurn]
		default:
			myTurn = opponentTurn
		}

		myScore := turnTypeScoreMap[myTurn]
		roundScore := myScore + turnResultScoreMap[myTurnResult]
		totalScore += roundScore
	}

	utils.ReadFile(dataFilePath, calculateScore)

	fmt.Printf("New Total Score: %d\n", totalScore)
}

func main() {
	part1()
	part2()
}
