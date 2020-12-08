import os
import sys


def main():
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(f'{parentdir}/..')

    try:
        from Data import getData as importData
    except ImportError:
        print("Unable to import AOCD Code")
        exit()

    if importData.check_file() is False:
        data = importData.get_todays_data(1, 2020)
        importData.write_data(data)
    else:
        data = importData.read_data()

    for i in range(0, len(data)-2):
        one = int(data[i])
        for j in range(i+1, len(data)-1):
            two = int(data[j])
            for k in range(j+1, len(data)):
                three = int(data[k])
                if one + two + three == 2020:
                    product = one * two * three
                    print(f'The numbers are {one}, {two}, and {three}.')
                    print(f'The product is {product}')
                    exit()


if __name__ == "__main__":
    main()
