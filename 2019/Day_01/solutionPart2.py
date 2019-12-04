import sys
from os import path

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

data = newData = []

if check_file() == False:
    data = get_todays_data(1,2019)
    write_data(data)
else:
    data = read_data()

for item in data:
    current_total = total_needed = last_calculated = fuel = int((int(item)/3))-2
    if fuel < 0:
        fuel = 0
    current_total = total_needed = last_calculated = fuel
    while True:
        fuel_needed = int((int(last_calculated)/3))-2
        if fuel_needed < 0:
            fuel_needed = 0
        last_calculated = fuel_needed
        current_total += fuel_needed
        if fuel_needed == 0:
            newData.append(current_total)
            break
print(str(sum(newData)))