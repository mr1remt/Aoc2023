input = open('Day 4\input.txt')
totSum = 0
repetitions = [1]*218
index = 0
for line in input:
	lineList = line.split()
	winningNums = []
	myNums = False
	winningSum = 0
	for i in range(len(lineList)):
		currNum = lineList[i]
		if i > 1:
			if currNum == "|":
				myNums = True
			if myNums:
				for winNum in winningNums:
					if currNum == winNum:
						winningSum += 1
			elif not myNums:
				winningNums.append(currNum)
	
	for rep in range(repetitions[index]):
		for i in range(winningSum):
			repetitions[index+i+1] += 1
		totSum += 1
	
	index +=1
	
print(totSum)
