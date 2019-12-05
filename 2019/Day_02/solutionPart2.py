import sys
from os import path

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

data = []

if check_file() == False:
    data = get_todays_data(2,2019)
    write_data(data)
else:
    data = read_data()

data = [int(x) for x in data[0].split(',')]
data[1] = 12
data[2] = 2

count = 0
while True:
    action = data[count]
    index_one = count + 1
    index_two = count + 2
    store_index = count + 3
    if action != 1 and action != 2:
        break
    data[data[store_index]] = data[data[index_one]] + data[data[index_two]] if action == 1 else data[data[index_one]] * data[data[index_two]]
    count += 4

print(data[0])    