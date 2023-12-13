possibleGames = 0
input = open('Day 2\input.txt')
for line in input:
	for char in [",",";",":"]:
		line = line.replace(char, " " + char)
	lineList = line.split()
	lineList.pop(0) 
	rgbList = [0,0,0]
	prevNum = 0
	possible = True
	for item in lineList:
		if item.isdigit():
			if item == lineList[0]:
				continue
			prevNum = int(item)
		else: 
			if item == "red":
				rgbList[0] = rgbList[0] + prevNum
			if item == "green":
				rgbList[1] = rgbList[1] + prevNum
			if item == "blue":
				rgbList[2] = rgbList[2] + prevNum
			if item == ";":
				if rgbList[0] <= 12 and rgbList[1] <= 13 and rgbList[2] <= 14 and possible == True:
					rgbList = [0,0,0]
					possible = True
				else:
					possible = False
	if rgbList[0] <= 12 and rgbList[1] <= 13 and rgbList[2] <= 14 and possible == True:
		possibleGames += int(lineList[0])
print(possibleGames)
