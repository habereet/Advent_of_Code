import sys
from os import path

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

if __name__ == "__main__":
    total = 0
    orbitDict = {}
    data = pull_data(6, 2019)
    for pair in data:
        current = list(pair.split(")"))
        orbitDict[current[1]] = current[0]
    for key in orbitDict.keys():
        currentKey = key
        while True:
            total += 1
            if orbitDict[currentKey] in orbitDict.keys():
                currentKey = orbitDict[currentKey]
            else:
                break
    print(total)