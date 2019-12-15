# I had some difficulty in calculating the orbitaltransfers so I took inspiration from
# u/vodak at r/adventofcode
# https://www.reddit.com/r/adventofcode/comments/e6tyva/2019_day_6_solutions/f9v4z6a?utm_source=share&utm_medium=web2x

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
    orbitDict = {}
    orbitList = []
    orbitalPath01 = []
    orbitalPath02 = []
    data = pull_data(6, 2019)
    # data = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]
    for pair in data:
        current = list(pair.split(")"))
        orbitDict[current[1]] = current[0]



you_orbit = 'YOU'
san_orbit = 'SAN'

you_orbits = []
san_orbits = []

while you_orbit in orbitDict:
    you_orbits.append(orbitDict[you_orbit])
    you_orbit = orbitDict[you_orbit]

while san_orbit in orbitDict:
    san_orbits.append(orbitDict[san_orbit])
    san_orbit = orbitDict[san_orbit]

print(you_orbits)
print(san_orbits)

transfer_count = min([you_orbits.index(orbit) + san_orbits.index(orbit) for orbit in set(you_orbits) & set(san_orbits)])

print('answer 2:', transfer_count)