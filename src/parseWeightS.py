import sys
import json

weightPath = sys.argv[1]

weightFile = open(weightPath, 'r')

print weightFile.readline()
print weightFile.readline()

dictPath = '../data/dict/dict36761.json'
dictFile = open(dictPath, 'r')
dictList = json.load(dictFile)
#word = dictList[int(index)]

D = dict()

for line in weightFile.readlines():
	l = line.strip().split('\t')
	if len(l) == 3:
		index = int(filter(lambda x: x.isdigit(),l[1]))
		stock =filter(lambda x: not x.isdigit(),l[1])
		D[(dictList[index][0], stock)] = int(l[0]) * float(l[2])

weightFile.close()

sortedDict = sorted(D.iteritems(), key = lambda x: x[1])
bottom = sortedDict[:20]
top = sortedDict[-1:-20:-1]

for item in top:
	print '%s\t%s\t%f\n' %(item[0][0], item[0][1], item[1])

for item in bottom:
	print '%s\t%s\t%f\n' %(item[0][0], item[0][1], item[1])

