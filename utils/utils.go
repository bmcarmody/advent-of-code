package utils

import (
	"bufio"
	"log"
	"os"
	"path/filepath"
)

func ReadFile(fileName string, callback func(string)) {
	currentDir, err := os.Getwd()
	CheckError("Error getting current directory:", err)

	filePath := filepath.Join(currentDir, fileName)
	file, err := os.Open(filePath)

	CheckError("Error opening file:", err)

	defer file.Close()
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		callback(scanner.Text())
	}

	CheckError("Error scanning file:", scanner.Err())
}

func CheckError(message string, err error) {
	if err != nil {
		log.Fatalf("\"%s\" %s", message, err)
	}
}
