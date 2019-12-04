from collections import Counter
from itertools import combinations

def read_file():
	with open("../box_data.txt") as file:
		lines = file.readlines()

	lines = [line.strip() for line in lines] 

	return lines

boxIDs = read_file()

boxIDCount = len(boxIDs)
boxIDLength = len(boxIDs[0])

for boxIDSet in combinations(boxIDs, 2):
	discrepancyCount = 0
	count = 0
	goodBoxIDLetters=""
	while count < boxIDLength:
		if boxIDSet[0][count] != boxIDSet[1][count] and discrepancyCount < 1:
			discrepancyCount += 1
			count += 1
		elif boxIDSet[0][count] != boxIDSet[1][count] and discrepancyCount == 1:
			break
		else:
			goodBoxIDLetters = f'{goodBoxIDLetters}{boxIDSet[0][count]}'
			count += 1
	if count == boxIDLength:
		goodGroup = (goodBoxIDLetters, boxIDSet[0], boxIDSet[1])
		print(goodGroup)

print(f'The remaining set of letters is: {goodGroup[0]}\nThis came from {goodGroup[1]} and {goodGroup[2]}')