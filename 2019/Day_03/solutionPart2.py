import sys
from os import path
import collections

loc = collections.namedtuple("coordinates", 'x y')
origin = loc(x=0, y=0)

wires = {}
distanceTracker = {}

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

def chaseWire(wire):
    wireTurns = []
    distance = 1
    distanceTracker = {}
    wireTurns.append(loc(x=0, y=0))
    steps = wire.split(',')
    for step in steps:
        currentLoc = wireTurns[-1]
        direction = step[0]
        number = int(step[1:])
        if direction == 'R':
            for x in range(1, number + 1):
                thisPos = loc(x=currentLoc.x + x, y=currentLoc.y)
                wireTurns.append(thisPos)
                distanceTracker[thisPos] = distance
                distance+=1
        elif direction == 'D':
            for x in range(1, number + 1):
                thisPos = loc(x=currentLoc.x, y=currentLoc.y - x)
                wireTurns.append(thisPos)
                distanceTracker[thisPos] = distance
                distance+=1
        elif direction == 'L':
            for x in range(1, number + 1):
                thisPos = loc(x=currentLoc.x - x, y=currentLoc.y)
                wireTurns.append(thisPos)
                distanceTracker[thisPos] = distance
                distance+=1
        elif direction == 'U':
            for x in range(1, number + 1):
                thisPos = loc(x=currentLoc.x, y=currentLoc.y + x)
                wireTurns.append(thisPos)
                distanceTracker[thisPos] = distance
                distance+=1
    return wireTurns, distanceTracker

def common_member(a, b):
    return list(set(a) & set(b))

def find_shortest_distance(points, distances):
    shortest = 10000000000
    for point in points:
        # print(distances[0][point])
        # print(distances[1][point])
        distance = distances[0][point] + distances[1][point]
        shortest = distance if distance < shortest else shortest
    print(shortest)

data = []

if check_file() == False:
    data = get_todays_data(3,2019)
    write_data(data)
else:
    data = read_data()

# data = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
# data = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]

for count, wire in enumerate(data):
    wires[count], distanceTracker[count] = chaseWire(wire)
intersections = common_member(wires[0], wires[1])
intersections.remove(loc(x=0, y=0))
find_shortest_distance(intersections, distanceTracker)