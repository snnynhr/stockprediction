import os
import random
import json
import creg_driver
import operator
import sys

datadir = '../XYdata/3'

stockfile = open(datadir + '/' + 'stock.txt', 'r')
stockList = stockfile.readline().strip().split('\t')
print "there are", len(stockList), "stocks"
stockfile.close()

l1 = sys.argv[1]

weightdir = '%s/weight%s' % (datadir, l1)
if not os.path.exists(weightdir):
    os.makedirs(weightdir)

resultdir = '%s/result%s' % (datadir, l1)
if not os.path.exists(resultdir):
    os.makedirs(resultdir)

pythonFile = 'regMainBs.py'

count = 0
for stock in stockList:
    print 'python %s %s %s %s %s %s &' % (pythonFile, l1, datadir, weightdir, resultdir, stock)
    count += 1
    if count % 8 == 0:
        print 'wait'
