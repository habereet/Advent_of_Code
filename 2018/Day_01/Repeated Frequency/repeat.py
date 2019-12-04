def read_file():
	with open("..\box_data.txt") as file:
		lines = file.readlines()

	lines = [line.strip() for line in lines] 

	return lines

calibrations = read_file()
total = 0
repeatedFrequency = 0
used_frequencies = {}
while True:
	for calibration in calibrations:
		if calibration[0] == "+":
			totalBefore = total
			totalAfter = totalBefore + int(calibration[1:])
			total = totalAfter
		else:
			totalBefore = total
			totalAfter = totalBefore - int(calibration[1:])
			total = totalAfter
		if total in used_frequencies.keys():
			repeatedFrequency = total
			break
		else:
			used_frequencies[total] = 1
	if repeatedFrequency == total:
		break
print(f'Repeated Frequency: {total}\nCalibrations Required: {len(used_frequencies.keys())}')
