import os
import sys


def importData(day, year):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(f'{parentdir}/..')

    try:
        from Data import getData as importData
    except ImportError:
        print("Unable to import AOCD Code")
        exit()

    if importData.check_file() is False:
        data = importData.get_todays_data(day, year)
        importData.write_data(data)
    else:
        data = importData.read_data()
    return data


def importTestData():
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(f'{parentdir}/..')

    try:
        from Data import getData as importData
    except ImportError:
        print("Unable to import AOCD Code")
        exit()

    if importData.check_file("testData.csv") is False:
        print("Exiting - TestData not found")
        exit()
    else:
        return importData.read_data("testData.csv")


def calcSeatID(seatInformation):
    lowerLimit = 0
    upperLimit = 127
    row = 0
    column = 0
    for item in range(7):
        choices = upperLimit - lowerLimit + 1
        if seatInformation[item] == 'F':
            upperLimit -= int(choices / 2)
        else:
            lowerLimit += int(choices / 2)
    row = lowerLimit
    lowerLimit = 0
    upperLimit = 7
    for item in range(7, 10):
        choices = upperLimit - lowerLimit + 1
        if seatInformation[item] == 'L':
            upperLimit -= int(choices / 2)
        else:
            lowerLimit += int(choices / 2)
    column = lowerLimit
    seatID = (row * 8) + column
    return(row, column, seatID)


def part_one(myData):
    print("----Part 01----")
    highest = 0
    for seat in myData:
        seatInfo = calcSeatID(seat)
        if seatInfo[2] > highest:
            highest = seatInfo[2]
    print(f'Highest Seat ID is - {highest}')


def part_two(myData):
    print("----Part 02----")
    IDs = []
    for seat in myData:
        seatInfo = calcSeatID(seat)
        IDs.append(seatInfo[2])
    IDs = sorted(IDs)
    for element in range(IDs[0], IDs[-1] + 1):
        if element not in IDs:
            print(f'Your Seat ID is - {element}')
            break


if __name__ == "__main__":
    dataset = importTestData() if len(sys.argv) == 2 else importData(5, 2020)
    part_one(dataset)
    part_two(dataset)
