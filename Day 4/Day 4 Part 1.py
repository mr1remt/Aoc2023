input = open('Day 4\input.txt')
totSum = 0
for line in input:
	lineList = line.split()
	winningNums = []
	myNums = False
	sum = 0
	for i in range(len(lineList)):
		currNum = lineList[i]
		if i > 1:
			if currNum == "|":
				myNums = True
			if myNums:
				for winNum in winningNums:
					if currNum == winNum:
						if sum == 0:
							sum = 1
						else: 
							sum = sum*2
			elif not myNums:
				winningNums.append(currNum)
	totSum += sum
print(totSum)