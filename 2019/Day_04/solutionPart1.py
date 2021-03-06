import sys
from os import path

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

def getPossiblePasswords(start, end):
    return list(range(start, end+1))

def splitIntegerIntoDigits(myNumber):
    return [int(number) for number in str(myNumber)]

def checkForEqualNumbers(myNumber):
    myList = splitIntegerIntoDigits(myNumber)
    if myList[0] == myList[1] or myList[1] == myList[2] or myList[2] == myList[3] or myList[3] == myList[4] or myList[4] == myList[5]:
        return True
    else:
        return False

def checkForAscendingValue(myNumber):
    myList = splitIntegerIntoDigits(myNumber)
    if myList[5] >= myList[4] >= myList[3] >= myList[2] >= myList[1] >= myList[0]:
        return True
    else:
        return False

def runAllTests(myNumber):
    if checkForAscendingValue(myNumber) == True and checkForEqualNumbers(myNumber) == True:
        return True
    else:
        return False

if __name__ == "__main__":
    data = pull_data(4, 2019)[0].split("-")
    myList = []
    for number in getPossiblePasswords(int(data[0]), int(data[1])):
        if runAllTests(number) == True:
            myList.append(number)
    print(len(myList))