# I had issues understanding the instructions for this one so I
# used Musical Muze's code in the Advent of Code subreddit 
# (https://www.reddit.com/r/adventofcode/comments/e6carb/2019_day_5_solutions/f9ubunk?utm_source=share&utm_medium=web2x 
# https://pastebin.com/MNgQq6YC )
# as a template and beginning

import sys
from os import path

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

# This returns the intcode
# intCode[3] && intCode[4] represent the opCode
# intCode[2] represents the mode of the first parameter (directly following intcode)
# intCode[1] represents the mode of the second parameter (directly following the first parameter)(if needed)
# intcode[0] represents the mode for the target if needed (directly following the second parameter)(if needed)
# examples follow:
# 1001, 2, 3, 4
# 01001 = intCode
# 01 = opCode
# 0 represents mode for 2
# 1 represents mode for 3
# 0 represents mode for 4
def getFiveDigitIntCode(valueToConvert):
    intCode = list(str(valueToConvert))
    while(len(intCode)) < 5:
        intCode.insert(0, 0)
    intCode = [int(item) for item in intCode]
    return intCode
    
def value(data, mode, index):
    if mode == 0:
        return data[data[index]]
    else:
        return data[index]

def increaseValueByTwo(originalValue):
    return originalValue + 2

def increaseValueByFour(originalValue):
    return increaseValueByTwo(increaseValueByTwo(originalValue))

def addition(data, index, firstIntCodeValue, secondIntCodeValue):
    firstNumber = value(data, secondIntCodeValue, index+1)
    secondNumber = value(data, firstIntCodeValue, index+2)
    data[data[index+3]] = firstNumber + secondNumber
    return (data, increaseValueByFour(index))

def multiply(data, index, firstIntCodeValue, secondIntCodeValue):
    firstNumber = value(data, secondIntCodeValue, index+1)
    secondNumber = value(data, firstIntCodeValue, index+2)
    data[data[index+3]] = firstNumber * secondNumber
    return (data, increaseValueByFour(index))
    
def userInput(data, valueFromIntCode, index):
    while True:
        try:
            userInput = int(input("What is the input: "))
        except:
            print("That's not a valid choice")
        if type(userInput) == int:
            break
    if valueFromIntCode == 0:
        data[data[index+1]] = userInput
    else:
        data[index+1] = userInput
    return (data, increaseValueByTwo(index))
    
def printIntCodeData(data, valueFromIntCode, index):
    print(value(data, valueFromIntCode, index))
    return increaseValueByTwo(index - 1)
    
    


if __name__ == "__main__":
    index = 0
    data = [int(item) for item in pull_data(5, 2019)[0].split(",")]
    while(data[index] != 99):
        intCode = getFiveDigitIntCode(data[index])
        if intCode[4] == 1:
            # Add
            data, index = addition(data, index, intCode[1], intCode[2])
        elif intCode[-1] == 2:
            # Multiply
            data, index = multiply(data, index, intCode[1], intCode[2])
        elif intCode[4] == 3:
            # Get input from user
            data, index = userInput(data, intCode[2], index)
        elif intCode[4] == 4:
            # Output
            index = printIntCodeData(data, intCode[2], index + 1)
