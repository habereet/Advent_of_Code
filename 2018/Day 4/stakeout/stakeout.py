def read_file(filePath):
	with open(filePath) as file:
		lines = file.readlines()

	lines = [line.strip() for line in lines] 

	return lines

guardData = sorted(read_file("..\guard_data.txt"))
print(guardData)