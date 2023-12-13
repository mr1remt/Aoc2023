possibleGames = 0
sum = 0

def isItBigger(currNums, maxNums):
	for i in [0,1,2]:
		if currNums[i] > maxNums[i]: maxNums[i] = currNums[i]
	return currNums, maxNums

input = open('Day 2\input.txt')
for line in input:
	for char in [",",";",":"]:
		line = line.replace(char, " " + char)
	lineList = line.split()
	lineList.pop(0) 
	rgbList = [0,0,0]
	highestNums = [0,0,0]
	prevNum = 0
	possible = True
	for item in lineList:
		if item.isdigit():
			prevNum = int(item)
		else: 
			if item == "red": 
				rgbList[0] = rgbList[0] + prevNum
				rgbList, highestNums = isItBigger(rgbList, highestNums)
			if item == "green":
				rgbList[1] = rgbList[1] + prevNum
				rgbList, highestNums = isItBigger(rgbList, highestNums)
			if item == "blue":
				rgbList[2] = rgbList[2] + prevNum
				rgbList, highestNums = isItBigger(rgbList, highestNums)
			if item == ";":
				if rgbList[0] <= 12 and rgbList[1] <= 13 and rgbList[2] <= 14 and possible == True:
					rgbList = [0,0,0]
					possible = True
				else: 
					rgbList = [0,0,0]
					possible = False
	if rgbList[0] <= 12 and rgbList[1] <= 13 and rgbList[2] <= 14 and possible == True:
		possibleGames += int(lineList[0])
	sum += highestNums[0] * highestNums[1] * highestNums[2]
print(possibleGames, sum)
