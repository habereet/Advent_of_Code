import sys
from os import path
from collections import Counter

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

def getPossiblePasswords(start, end):
    return list(range(start, end+1))

def splitIntegerIntoDigits(myNumber):
    return [int(number) for number in str(myNumber)]

def checkForEqualNumbers(myNumber):
    # Break number into its individual digits
    myString = str(myNumber)
    # Build a list of repeated numbers
    listOfRepeatedLetters = []
    # iterate through the numbers pairwise
    for letterOne, letterTwo in zip(myString, myString[1:]):
        if letterOne == letterTwo:
            # if the pair is equal add it to listOfRepeatedLetters
            listOfRepeatedLetters.append(letterOne)
    # If '1' is found in the counter, return true; we've found a pair.
    if 1 in Counter(listOfRepeatedLetters).values():
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