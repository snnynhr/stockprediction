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

weightPath = '%s/%s.txt' %(weightdir, stock)
weightFile = open(weightPath, 'w')
weightFile.close() 

resultPath = '%s/%s.txt' %(resultdir, stock)
resultfile = open(resultPath, 'w')

results = creg_driver.evaluate((trainXPath, trainYPath), (devXPath, devYPath), options={"--l1": l1, "--z":weightPath})
accuracy = round(float(sum(map(lambda v: 1 if v['true_label'] == v['predicted_label'] else 0, results.values()))) / len(results),4)

resultfile.write('%s\t%d\n' %(stock, accuracy))
resultfile.close()
print stock, accuracy

       

