import sys
import json
import os

weightDir = '../XYdata/3/weight1'
resultDir = '../XYdata/3/weightResult'
pythonFile = 'parseWeightS.py'

count = 0
for filename in os.listdir(weightDir):
	weightPath = '%s/%s' % (weightDir, filename)
	resultPath = '%s/%s' % (resultDir, filename)
	print 'python %s %s > %s' % (pythonFile, weightPath, resultPath)
	if count%5 == 0:
		print 'wait'


