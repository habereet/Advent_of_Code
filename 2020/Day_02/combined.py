import os
import sys
import re


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


def part_one(myData):
    print("----Part 01----")
    validPasswords = 0
    p = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]*)")
    for i in myData:
        m = p.match(i)
        lowerBound = int(m.group(1))
        upperBound = int(m.group(2))
        checkChar = m.group(3)
        hash = m.group(4)
        if lowerBound <= hash.count(checkChar) <= upperBound:
            validPasswords += 1
    print(f'The number of valid passwords is {validPasswords}')


def part_two(myData):
    print("----Part 02----")
    validPasswords = 0
    p = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]*)")
    for i in myData:
        m = p.match(i)
        lowerIndex = int(m.group(1)) - 1
        upperIndex = int(m.group(2)) - 1
        checkChar = m.group(3)
        hash = m.group(4)
        if (
               (True if hash[lowerIndex] == checkChar else False)
               ^
               (True if hash[upperIndex] == checkChar else False)
           ):
            validPasswords += 1
    print(f'The number of valid passwords is {validPasswords}')


if __name__ == "__main__":
    dataset = importData(2, 2020)
    part_one(dataset)
    part_two(dataset)
