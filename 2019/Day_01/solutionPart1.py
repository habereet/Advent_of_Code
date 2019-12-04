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
    newData.append(int((int(item)/3))-2)
print(str(sum(newData)))