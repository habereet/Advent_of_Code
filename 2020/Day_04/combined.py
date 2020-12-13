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


def part_one(myData):
    print("----Part 01----")
    batchFile = ""
    matchingPassports = 0
    for i in myData:
        if i != "":
            batchFile = batchFile + i + " "
        else:
            if (
                "ecl:" in batchFile
                and "pid:" in batchFile
                and "eyr:" in batchFile
                and "hcl:" in batchFile
                and "byr:" in batchFile
                and "iyr:" in batchFile
                and "hgt:" in batchFile
            ):
                matchingPassports += 1
            batchFile = ""
    print('The number of valid passports is '
          f'- {matchingPassports}')


def part_two(myData):
    print("----Part 02----")


if __name__ == "__main__":
    dataset = importTestData() if len(sys.argv) == 2 else importData(4, 2020)
    part_one(dataset)
    part_two(dataset)
