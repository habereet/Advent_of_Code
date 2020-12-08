from aocd import get_data
from os import path


def get_todays_data(dy, yr):
    try:
        data = get_data(day=dy, year=yr)
    except Exception:
        return "No Data"
    return data.split("\n")


def check_file(file_name="data.csv"):
    return path.isfile(file_name)


def read_data(file_name="data.csv"):
    with open(file_name) as file:
        content = file.readlines()
    return [x.strip() for x in content]


def write_data(todays_data):
    if type(todays_data) != list:
        return "Incorrect Data"
    else:
        file = open("data.csv", "w")
        for line in todays_data:
            file.write(f'{line}\n')
        file.close()


def pull_data(day, year):
    if check_file() is False:
        data = get_todays_data(day, year)
        write_data(data)
    else:
        data = read_data()
    return data


def main():
    print(get_todays_data(1, 2019))


if __name__ == "__main__":
    main()
