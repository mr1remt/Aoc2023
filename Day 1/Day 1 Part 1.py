sum = 0
tSum = ""

with open('Day 1\input.txt') as input:
	lines = input.readlines()
	for line in lines:
		for char in line:
			if char.isdigit():
				tSum = char
				break
		for char in line[::-1]:
			if char.isdigit():
				tSum += char
				break
		sum += int(tSum)
	print(sum)
