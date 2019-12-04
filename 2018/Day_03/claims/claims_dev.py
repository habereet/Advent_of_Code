import re
from collections import namedtuple
from collections import Counter

clothDimensions = 6

def read_file(filePath):
	with open(filePath) as file:
		lines = file.readlines()

	lines = [line.strip() for line in lines] 

	return lines
	
def get_claim_data(line, pattern):
	claimMatch = pattern.match(line)
	thisClaim = claim(claimMatch.group(1), claimMatch.group(2), claimMatch.group(3), claimMatch.group(4), claimMatch.group(5))
	return thisClaim

def cut_cloth(dimensions):
	cloth = []
	for x in range(0, dimensions + 2):
		row = []
		for y in range(0, dimensions + 2):
			row.append(".")
		cloth.append(row)
	return cloth

def ship_cloth(dimensions, cloth):
	for y in range(0, dimensions + 2):
		print(cloth[y])

cloth = cut_cloth(clothDimensions)
claim = namedtuple('claim', 'claimNumber fromLeft fromTop width heigth')
pattern = re.compile('\#(\d*) \@ (\d*),(\d*)\: (\d*)x(\d*)')
claimList = []

for currentClaim in read_file("../claims_data_test.txt"):
	claimList.append(get_claim_data(currentClaim, pattern))

print(f'Cloth with no claims:')
ship_cloth(clothDimensions, cloth)

for currentClaim in list(claimList):
	x = int(currentClaim.fromLeft)
	y = int(currentClaim.fromTop)
	for height in range(0, int(currentClaim.heigth)):
		for width in range(0, int(currentClaim.width)):
			if cloth[height + y][width + x] == '.':
				cloth[height + y][width + x] = currentClaim.claimNumber
			else:
				cloth[height + y][width + x] = 'X'
				
print(f'\nCloth with all claims:')
ship_cloth(clothDimensions, cloth)
print(f'\nSquare inches with multiple claims: {sum(row.count("X") for row in cloth)}')