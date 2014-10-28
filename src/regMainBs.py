import os
import random
import json
import creg_driver
import operator
import sys

l1 = sys.argv[1]
datadir = sys.argv[2]
weightdir = sys.argv[3]
resultdir = sys.argv[4]
stock = sys.argv[5]

fulldir = datadir + '/full'
testdir = datadir + '/test'
traindir = datadir + '/train'
devdir = datadir + '/dev'

resultfile = open('%s/resultl1=%s.txt' %(datadir, l1), 'w')  

print "learning for %s ..." %stock
trainXPath = traindir + '/' + stock + 'x'
trainYPath = traindir + '/' + stock + 'y'

testXPath = testdir + '/' + stock + 'x'
testYPath = testdir + '/' + stock + 'y'

devXPath = devdir + '/' + stock + 'x'
devYPath = devdir + '/' + stock + 'y'

devYfile = open(devYPath, 'r')
deCount = 0
inCount = 0
pairs = [ line.strip().split('\t') for line in devYfile.readlines()]
deCount = len(filter(lambda x: x[1] == "-1", pairs))
inCount = len(filter(lambda x: x[1] == "1", pairs))
total = deCount + inCount
dePer = round(float(deCount)/total, 4)
inPer = round(float(inCount)/total, 4)
devYfile.close()

resultPath = '%s/%s.txt' %(resultdir, stock)
resultfile = open(resultPath, 'w')

weightPath = '%s/%s.txt' %(weightdir, stock)
if os.path.isfile(weightPath):
	results = creg_driver.evaluate((trainXPath, trainYPath), (devXPath, devYPath), options={"--l1": l1, "-w":weightPath})

else:
	weightFile = open(weightPath, 'w')
	weightFile.close() 

	results = creg_driver.evaluate((trainXPath, trainYPath), (devXPath, devYPath), options={"--l1": l1, "--z":weightPath})

accuracy = round(float(sum(map(lambda v: 1 if v['true_label'] == v['predicted_label'] else 0, results.values()))) / len(results),4)

resultfile.write('%s\t%d\t%f\t%f\t%f\n' %(stock, total, dePer, inPer, accuracy))
resultfile.close()
print stock, accuracy

       

