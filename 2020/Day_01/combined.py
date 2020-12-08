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


def part_one(myData):
    print("----Part 01----")
    for i in range(0, len(myData)-2):
        one = int(myData[i])
        for j in range(i+1, len(myData)-1):
            two = int(myData[j])
            if one + two == 2020:
                product = one * two
                print(f'The numbers are {one} and {two}.')
                print(f'The product is {product}')
                return


def part_two(myData):
    print("----Part 02----")
    for i in range(0, len(myData)-2):
        one = int(myData[i])
        for j in range(i+1, len(myData)-1):
            two = int(myData[j])
            for k in range(j+1, len(myData)):
                three = int(myData[k])
                if one + two + three == 2020:
                    product = one * two * three
                    print(f'The numbers are {one}, {two}, and {three}.')
                    print(f'The product is {product}')
                    return


if __name__ == "__main__":
    dataset = importData(1, 2020)
    part_one(dataset)
    part_two(dataset)
