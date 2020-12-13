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
    if myData[-1] != "":
        myData.append("")
    batchFile = ""
    matchingPassports = 0
    for i in myData:
        if i != "":
            batchFile = batchFile + i + " "
        else:
            byr = re.search(r"byr:(\d{4})", batchFile)
            iyr = re.search(r"iyr:(\d{4})", batchFile)
            eyr = re.search(r"eyr:(\d{4})", batchFile)
            hgt = re.search(r"hgt:(\d+)([cmin]+)", batchFile)
            hcl = re.search(r"hcl:#[0-9a-f]{6}", batchFile)
            ecl = re.search(r"ecl:([a-z]{3})", batchFile)
            pid = re.search(r"pid:([0-9]+)", batchFile)
            if (
                byr
                and 1920 <= int(byr.group(1)) <= 2002
                and iyr
                and 2010 <= int(iyr.group(1)) <= 2020
                and eyr
                and 2020 <= int(eyr.group(1)) <= 2030
                and checkHeight(hgt)
                and hcl
                and checkEyeColor(ecl)
                and pid
                and len(pid.group(1)) == 9
            ):
                matchingPassports += 1
            batchFile = ""
    print('The number of valid passports is '
          f'- {matchingPassports}')


def checkEyeColor(ecl):
    eyeColorList = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if (
        ecl
        and ecl.group(1) in eyeColorList
    ):
        return True
    else:
        return False


def checkHeight(hgt):
    if not hgt:
        return False
    elif hgt.group(2) == "cm":
        return True if 150 <= int(hgt.group(1)) <= 193 else False
    elif hgt.group(2) == "in":
        return True if 59 <= int(hgt.group(1)) <= 76 else False
    else:
        return False


if __name__ == "__main__":
    dataset = importTestData() if len(sys.argv) == 2 else importData(4, 2020)
    part_one(dataset)
    part_two(dataset)
