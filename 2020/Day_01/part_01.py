import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(f'{parentdir}/..')

try:
    from Data import getData as importData
except ImportError:
    print("Unable to import AOCD Code")
    exit()

data = newData = []

if importData.check_file() is False:
    data = importData.get_todays_data(1, 2020)
    importData.write_data(data)
else:
    data = importData.read_data()
