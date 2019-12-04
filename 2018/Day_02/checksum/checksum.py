from collections import Counter

def read_file():
	with open("../box_data.txt") as file:
		lines = file.readlines()

	lines = [line.strip() for line in lines] 

	return lines

boxIDs = read_file()

two_count = 0
three_count = 0

for boxID in boxIDs:
	if 2 in Counter(list(boxID)).values():
		two_count += 1
	if 3 in Counter(list(boxID)).values():
		three_count += 1
print(f'Words with the same letter twice: {two_count}\nWords with the same letter three times: {three_count}\nChecksum: {two_count * three_count}')