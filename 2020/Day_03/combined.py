import os
import sys
import math


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


def part_one(myData):
    print("----Part 01----")
    # x and 0 contro where we are on the hill
    # trees counts how many we've hit on the way down
    x = 0
    y = 0
    trees = 0
    # for each row
    for i in myData:
        # if it's the first row, move on to the second
        if y == 0:
            y += 1
        # otherwise
        else:
            length = len(i)
            # move 3 to the right
            x += 3
            # since the pattern extends to the right 'forever'
            # we mock this by shifting to the beginning of the
            # row when we hit the end
            x = x - length if x >= length else x
            # if we hit a tree increment the counter
            if i[x] == "#":
                trees += 1
            y += 1
    print(f'Number of trees - {trees}')


# Very similar to part 1 but we account for multiple slopes
# and run through with a for loop
def part_two(myData):
    print("----Part 02----")
    # list of slopes
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    # list of how many trees we hit with each slope
    treeList = []
    # for each slope
    for slope in slopes:
        # set the start values as ablove
        x = 0
        y = 0
        trees = 0
        # one of our rows has a slope that moves
        # two rows at a time. This accounts for it
        multiRow = False
        # grab slope values from slope
        right = slope[0]
        down = slope[1]
        # more or less copy and paste from part 1
        for i in myData:
            if y == 0:
                if down > 1:
                    # here we set the value if
                    # multiRow
                    multiRow = True
                y += 1
            else:
                # if multiRow, do now math
                if multiRow is True:
                    multiRow = False
                else:
                    if down > 1:
                        multiRow = True
                    length = len(i)
                    # instead of 3 in day 1, use right
                    x += right
                    x = x - length if x >= length else x
                    if i[x] == "#":
                        trees += 1
                    y += 1
        print(f'For slope ({right}, {down}),'
              f' the number of trees hit is - {trees}')
        treeList.append(trees)
    print(f'The multiple of all slopes is - {math.prod(treeList)}')


if __name__ == "__main__":
    dataset = importTestData() if len(sys.argv) == 2 else importData(3, 2020)
    # print(dataset)
    part_one(dataset)
    part_two(dataset)
