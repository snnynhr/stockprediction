import os
import random
import json
import creg_driver
import operator
import sys

datadir = '../XYdata/3'
fulldir = datadir + '/full'
testdir = datadir + '/test'
traindir = datadir + '/train'
devdir = datadir + '/dev'

if not os.path.exists(traindir):
    os.makedirs(traindir)

if not os.path.exists(devdir):
    os.makedirs(devdir)  

if not os.path.exists(testdir):
    os.makedirs(testdir)

stockfile = open(datadir + '/' + 'stock.txt','w+' )
pythonFile = 'partitionS.py'

count = 0
for filename in os.listdir(fulldir):
    if filename.endswith('json'):
        stock = filename[:-5]
        stockfile.write(stock + '\t')
        print'python %s %s %s &' %(pythonFile, datadir, stock)
        count += 1
        if count %4 == 0:
            print "wait"

stockfile.close()

