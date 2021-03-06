import sys
from os import path
from itertools import product

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

originalData = []

if check_file() == False:
    originalData = get_todays_data(2,2019)
    write_data(originalData)
else:
    originalData = read_data()

originalData = [int(x) for x in originalData[0].split(',')]
try:
    for noun, verb in product(range(100), range(100)):
        data = originalData.copy()
        data[1] = noun
        data[2] = verb
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
            if data[0] == 19690720:
                raise StopIteration
except StopIteration:
    print(f'{noun*100 + verb}')
    exit(0)
print("Couldn't identify inputs")