import sys
from os import path
import collections

loc = collections.namedtuple("coordinates", 'x y')
origin = loc(x=0, y=0)

wires = {}

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

def chaseWire(wire):
    wireTurns = []
    wireTurns.append(loc(x=0, y=0))
    steps = wire.split(',')
    for step in steps:
        currentLoc = wireTurns[-1]
        direction = step[0]
        number = int(step[1:])
        if direction == 'R':
            for x in range(1, number + 1):
                wireTurns.append(loc(x=currentLoc.x + x, y=currentLoc.y))
        elif direction == 'D':
            for x in range(1, number + 1):
                wireTurns.append(loc(x=currentLoc.x, y=currentLoc.y - x))
        elif direction == 'L':
            for x in range(1, number + 1):
                wireTurns.append(loc(x=currentLoc.x - x, y=currentLoc.y))
        elif direction == 'U':
            for x in range(1, number + 1):
                wireTurns.append(loc(x=currentLoc.x, y=currentLoc.y + x))
    return wireTurns

def common_member(a, b):
    return list(set(a) & set(b))

def find_shortest_manhattan(points):
    shortest = 10000000000
    for point in points:
        distance = abs(point.x) + abs(point.y)
        shortest = distance if distance < shortest else shortest
    print(shortest)

data = []

if check_file() == False:
    data = get_todays_data(3,2019)
    write_data(data)
else:
    data = read_data()

for count, wire in enumerate(data):
    wires[count] = chaseWire(wire)
intersections = common_member(wires[0], wires[1])
intersections.remove(loc(x=0, y=0))
find_shortest_manhattan(intersections)