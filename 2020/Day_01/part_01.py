import os
import sys


currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(f'{parentdir}/..')

#print(sys.path)

from Data import getData as importData

data = newData = []

if importData.check_file() == False:
    data = importData.get_todays_data(1,2020)
    importData.write_data(data)
else:
    data = importData.read_data()

