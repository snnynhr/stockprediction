import sys
import json
import codecs

weightPath = sys.argv[1]
resultPath = sys.argv[2]

weightFile = codecs.open(weightPath, 'r','utf-8')

resultFile = codecs.open(resultPath,'w','utf-8')


weightFile.readline()
weightFile.readline()

# title1 = unicode(weightFile.readline())
# title2 = unicode(weightFile.readline())
# resultFile.write(title1)
# resultFile.write(title2)

dictPath = '../data/dict/dict_lowered.json'
dictFile = codecs.open(dictPath, 'r','utf-8')
dictList = json.load(dictFile)
#word = dictList[int(index)]

D = dict()

for line in weightFile:
	l = line.strip().split('\t')
	if len(l) == 3:
		index = int(l[1].split('_')[1])
		stock = l[1].split('_')[0]
		#index = int(filter(lambda x: x.isdigit(),l[1]))
		#stock =filter(lambda x: not x.isdigit(),l[1])
		try:
			D[(dictList[index][0], stock)] = int(l[0]) * float(l[2])
		except:
			print l[0],l[1],l[2]
			print l

weightFile.close()

sortedDict = sorted(D.iteritems(), key = lambda x: x[1])
bottom = sortedDict[:20]
top = sortedDict[-1:-20:-1]

resultFile = codecs.open(resultPath,'w','utf-8')
for item in top:
	resultFile.write(u'%s\t%s\t%f\n' %(item[0][0], item[0][1], item[1]))

for item in bottom:
	resultFile.write(u'%s\t%s\t%f\n' %(item[0][0], item[0][1], item[1]))
resultFile.close()

