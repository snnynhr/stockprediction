import os
import random
import json

datadir = '../XYdata/1'
fulldir = datadir + '/full'
testdir = datadir + '/test'
traindir = datadir + '/train'
devdir = datadir + '/dev'

if not os.path.exists(testdir):
    os.makedirs(traindir)

if not os.path.exists(devdir):
    os.makedirs(devdir)  

if not os.path.exists(testdir):
    os.makedirs(testdir)

for filename in os.listdir(fulldir):
    if filename.endswith('json'):
        stock = filename[:-5]
        fullFile = open(fulldir + '/' + filename,'r')
        points = fullFile.readlines()
        total = len(points)
        print "%s have %d points in total" %(stock, total)

        random.shuffle(points)
        index1, index2 = int(0.7 * total), int(0.1 * total)
        train = points[:index1]
        dev = points[index1 : index2]
        test = points[index2:]

        trainXPath = traindir + '/' + filename + 'x'
        trainYPath = traindir + '/' + filename + 'y'
        trainXFile = open(trainXPath, 'w')
        trainYFile = open(trainYPath, 'w')
        for point in train:
            date, Y, X = json.loads(point)
            trainXFile.write(str(date) + '\t'+json.dumps(X) + '\n')
            trainYFile.write(str(date) + '\t' + str(Y) + '\n')
        trainXFile.close()
        trainYFile.close()

        testXPath = testdir + '/' + filename + 'x'
        testYPath = testdir + '/' + filename + 'y'
        testXFile = open(testXPath, 'w')
        testYFile = open(testYPath, 'w')
        for point in test:
            date, Y, X = json.loads(point)
            testXFile.write(str(date) + '\t'+json.dumps(X) + '\n')
            testYFile.write(str(date) + '\t' + str(Y) + '\n')
        testXFile.close()
        testYFile.close()

        devXPath = devdir + '/' + filename + 'x'
        devYPath = devdir + '/' + filename + 'y'
        devXFile = open(devXPath, 'w')
        devYFile = open(devYPath, 'w')
        for point in test:
            date, Y, X = json.loads(point)
            devXFile.write(str(date) + '\t'+json.dumps(X) + '\n')
            devYFile.write(str(date) + '\t' + str(Y) + '\n')
        devXFile.close()
        devYFile.close()
        break
