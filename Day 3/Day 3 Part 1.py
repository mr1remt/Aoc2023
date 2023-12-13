from enum import Enum

prevLine = []
currLine = []
allLines = []
currDigits = ""
sum = 0

class sType(Enum):
	num = 1
	sym = 2

class item:
	def __init__(self, type, val, start, end):
		self.type = type
		self.val = val
		self.start = start
		self.end = end
		self.isPart = False
	isPart: bool

prevChar: item

input = open('Day 3\input.txt')
for line in input:
	currLine = []
	for i in range(len(line)-1):
		# add all symbols and numbers into new list with indexes
		currChar = line[i]
		if currChar.isdigit():
			if not currLine:
				prevChar = item(sType.num, currChar, i, i)
				currLine.append(prevChar)
			else:
				if prevChar.type == sType.num:
					if prevChar.end == i-1:
						prevChar.val = int(str(prevChar.val) + currChar)
						prevChar.end = i
					else:
						prevChar = item(sType.num, currChar, i, i)
						currLine.append(prevChar)
				elif prevChar.type == sType.sym:
					prevChar = item(sType.num, currChar, i, i)
					currLine.append(prevChar)
		elif not currChar == ".":
			prevChar = item(sType.sym, currChar, i, i)
			currLine.append(prevChar)
	allLines.append(currLine)

for i in range(len(allLines)):
	for char in allLines[i]:
		# for every number
		if char.type == sType.num:
			# check all symbols on current line
			for sym in allLines[i]:
				if sym.type == sType.sym:
					if sym.start+1 == char.start or sym.start-1 == char.end:
						char.isPart = True
		# check current line symbols and numbers against previous line
		for prevChar in allLines[i-1]:
			if char.type == sType.num and prevChar.type == sType.sym:
				if prevChar.start+1 >= char.start and prevChar.start-1 <= char.end:
					char.isPart = True
			if char.type == sType.sym and prevChar.type == sType.num:
				if char.start+1 >= prevChar.start and char.start-1 <= prevChar.end:
					prevChar.isPart = True

for line in allLines:
	for num in line:
		if num.type == sType.num and num.isPart == True:
			sum += int(num.val)
print(sum)
