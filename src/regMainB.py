import os
import random
import json
import creg_driver
import operator
import sys

datadir = '../XYdata/2'
fulldir = datadir + '/full'
testdir = datadir + '/test'
traindir = datadir + '/train'
devdir = datadir + '/dev'
stockfile = open(datadir + '/' + 'stock.txt', 'r')
stockList = stockfile.readline().strip().split('\t')
print "there are", len(stockList), "stocks"
stockfile.close()


l1 = sys.argv[1]
print l1

weightdir = '%s/weight%s' % (datadir, l1)
if not os.path.exists(weightdir):
    os.makedirs(weightdir)

resultfile = open('%s/resultl1=%s.txt' % (datadir, l1), 'w')

for stock in stockList:
    print "learning for %s ..." % stock
    trainXPath = traindir + '/' + stock + 'x'
    trainYPath = traindir + '/' + stock + 'y'

    testXPath = testdir + '/' + stock + 'x'
    testYPath = testdir + '/' + stock + 'y'

    devXPath = devdir + '/' + stock + 'x'
    devYPath = devdir + '/' + stock + 'y'

    weightPath = '%s/%s.txt' % (weightdir, stock)
    weightFile = open(weightPath, 'a')
    weightFile.close()

    results = creg_driver.evaluate((trainXPath, trainYPath), (devXPath, devYPath), options={"--l1": l1, "--z": weightPath})
    accuracy = round(float(sum(map(lambda v: 1 if v['true_label'] == v['predicted_label'] else 0, results.values()))) / len(results), 4)

    resultfile.write('%s\t%d\n' % (stock, accuracy))
    print stock, accuracy

resultfile.close()
