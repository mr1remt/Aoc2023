sum = 0
tSum = ""
dict = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
foundNums = []

with open('Day 1\input.txt') as input:
	lines = input.readlines()
	for line in lines:
		for currChar in range(len(line)):
			# check digits, first from beginning	
			if line[currChar].isdigit():
				foundNums.append(line[currChar])
			# find numbers in text, first from beginning
			for letterLen in [3,4,5]:
				currLetters = ""
				# add letters to be checked
				for offset in range(letterLen):
					if currChar+offset >= len(line):
						break
					currLetters += line[currChar+offset]
				# if word matches dict
				for dictNums in range(len(dict)):
					if currLetters == dict[dictNums]:
						foundNums.append(dictNums+1)
		sum += int(str(foundNums[0]) + str(foundNums[len(foundNums)-1]))
		foundNums = []
	print(sum)
