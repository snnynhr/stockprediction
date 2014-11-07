import os
import random
import json
import creg_driver
import operator
import sys
import codecs


datadir = sys.argv[1]
stock = sys.argv[2]

fulldir = datadir + '/full'
testdir = datadir + '/test'
traindir = datadir + '/train'
devdir = datadir + '/dev'

filename = stock + '.json'

fullFile = codecs.open(fulldir + '/' + filename, 'r','utf-8')
points = fullFile.readlines()
total = len(points)
print "%s have %d points in total" % (stock, total)

random.shuffle(points)
index1, index2 = int(0.7 * total), int(0.1 * total)
train = points[:index1]
dev = points[index1: index2]
test = points[index2:]

trainXPath = traindir + '/' + stock + 'x'
trainYPath = traindir + '/' + stock + 'y'
trainXFile = codecs.open(trainXPath, 'w','utf-8')
trainYFile = codecs.open(trainYPath, 'w','utf-8')
for point in train:
    date, Y, X = json.loads(point)
    trainXFile.write(str(date) + '\t' + json.dumps(X) + '\n')
    trainYFile.write(str(date) + '\t' + str(Y) + '\n')
trainXFile.close()
trainYFile.close()

testXPath = testdir + '/' + stock + 'x'
testYPath = testdir + '/' + stock + 'y'
testXFile = codecs.open(testXPath, 'w','utf-8')
testYFile = codecs.open(testYPath, 'w','utf-8')
for point in test:
    date, Y, X = json.loads(point)
    testXFile.write(str(date) + '\t' + json.dumps(X) + '\n')
    testYFile.write(str(date) + '\t' + str(Y) + '\n')
testXFile.close()
testYFile.close()

devXPath = devdir + '/' + stock + 'x'
devYPath = devdir + '/' + stock + 'y'
devXFile = codecs.open(devXPath, 'w','utf-8')
devYFile = codecs.open(devYPath, 'w','utf-8')
for point in test:
    date, Y, X = json.loads(point)
    devXFile.write(str(date) + '\t' + json.dumps(X) + '\n')
    devYFile.write(str(date) + '\t' + str(Y) + '\n')
devXFile.close()
devYFile.close()
