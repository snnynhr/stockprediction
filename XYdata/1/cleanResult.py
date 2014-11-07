resultFile= open('result2.txt','r')
resultresultFile = open('resultComplete.txt','w')

lineList = resultFile.readlines()

lineNum = 0

totalLines = len(lineList)
print totalLines

stock = None
while lineNum< totalLines:
	line = lineList[lineNum].strip()
	numbers = line.split()
	if line.endswith('total'):
		words = numbers
		if int(words[2])<1000:
			lineNum += 2
	elif len(numbers) == 1:
		stock = line
	else:
		numbers = line.split()
		info = stock + '\t' + '\t'.join(numbers) + '\n'
		resultresultFile.write(info)
	lineNum += 1
