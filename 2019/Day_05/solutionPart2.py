import sys
from os import path

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

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
    # print("--ADDITION--")
    firstNumber = value(data, firstIntCodeValue, index+1)
    secondNumber = value(data, secondIntCodeValue, index+2)
    data[data[index+3]] = firstNumber + secondNumber
    return (data, increaseValueByFour(index))

def multiply(data, index, firstIntCodeValue, secondIntCodeValue):
    # print("--MULTIPLY--")
    firstNumber = value(data, firstIntCodeValue, index+1)
    secondNumber = value(data, secondIntCodeValue, index+2)
    data[data[index+3]] = firstNumber * secondNumber
    return (data, increaseValueByFour(index))
    
def userInput(data, valueFromIntCode, index):
    # print("--USER INPUT--")
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
    # print("--OUTPUT--)
    print(value(data, valueFromIntCode, index))
    return increaseValueByTwo(index - 1)
    
def jumpIfTrue(data, index, firstIntCodeValue, secondIntCodeValue):
    # print("--JUMP IF FALSE--")
    if value(data, firstIntCodeValue, index + 1) != 0:
        return (data, value(data, secondIntCodeValue, index + 2))
    else:
        return (data, index + 3)
    
def jumpIfFalse(data, index, firstIntCodeValue, secondIntCodeValue):
    # print("--JUMP IF FALSE--")
    if value(data, firstIntCodeValue, index + 1) == 0:
        return (data, value(data, secondIntCodeValue, index + 2))
    else:
        return (data, index + 3)
        
def lessThan(data, index, firstIntCodeValue, secondIntCodeValue):
    # print("--LESS THAN --"")
    if value(data, firstIntCodeValue, index + 1) < value(data, secondIntCodeValue, index + 2):
        data[data[index + 3]] = 1
    else:
        data[data[index + 3]] = 0
    return (data, index + 4)
    
def equals(data, index, firstIntCodeValue, secondIntCodeValue):
    # print("--EQUALS--")
    if value(data, firstIntCodeValue, index + 1) == value(data, secondIntCodeValue, index + 2):
        data[data[index + 3]] = 1
    else:
        data[data[index + 3]] = 0
    return (data, index + 4)
    
    


if __name__ == "__main__":
    index = 0
    data = [int(item) for item in pull_data(5, 2019)[0].split(",")]
    # data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    while(data[index] != 99):
        intCode = getFiveDigitIntCode(data[index])
        if intCode[4] == 1:
            # Add
            data, index = addition(data, index, intCode[2], intCode[1])
        elif intCode[-1] == 2:
            # Multiply
            data, index = multiply(data, index, intCode[2], intCode[1])
        elif intCode[4] == 3:
            # Get input from user
            data, index = userInput(data, intCode[2], index)
        elif intCode[4] == 4:
            # Output
            index = printIntCodeData(data, intCode[2], index + 1)
        elif intCode[4] == 5:
            # Jump if True
            data, index = jumpIfTrue(data, index, intCode[2], intCode[1])
        elif intCode[4] == 6:
            # Jump if False
            data, index = jumpIfFalse(data, index, intCode[2], intCode[1])
        elif intCode[4] == 7:
            # Less Than
            data, index = lessThan(data, index, intCode[2], intCode[1])
        elif intCode[4] == 8:
            # Equals
            data, index = equals(data, index, intCode[2], intCode[1])