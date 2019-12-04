def read_file():
	with open("..\box_data.txt") as file:
		lines = file.readlines()

	lines = [line.strip() for line in lines] 

	return lines

frequencies = read_file()
total = 0
for frequency in frequencies:
	if frequency[0] == "+":
		total = total + int(frequency[1:])
	else:
		total = total - int(frequency[1:])
print(f'Calibration: {total}')