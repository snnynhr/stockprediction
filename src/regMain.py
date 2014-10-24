import os
import random
import json
import creg_driver
import operator

datadir = '../XYdata/2'
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


l1List = [str(round(0.1 * x,1)) for x in xrange(1, 10)] + [str(x) for x in xrange(1, 10)]
l1Dict = dict([(x,0) for x in l1List])

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

        trainXPath = traindir + '/' + stock + 'x'
        trainYPath = traindir + '/' + stock + 'y'
        trainXFile = open(trainXPath, 'w')
        trainYFile = open(trainYPath, 'w')
        for point in train:
            date, Y, X = json.loads(point)
            trainXFile.write(str(date) + '\t'+json.dumps(X) + '\n')
            trainYFile.write(str(date) + '\t' + str(Y) + '\n')
        trainXFile.close()
        trainYFile.close()

        testXPath = testdir + '/' + stock + 'x'
        testYPath = testdir + '/' + stock + 'y'
        testXFile = open(testXPath, 'w')
        testYFile = open(testYPath, 'w')
        for point in test:
            date, Y, X = json.loads(point)
            testXFile.write(str(date) + '\t'+json.dumps(X) + '\n')
            testYFile.write(str(date) + '\t' + str(Y) + '\n')
        testXFile.close()
        testYFile.close()

        devXPath = devdir + '/' + stock + 'x'
        devYPath = devdir + '/' + stock + 'y'
        devXFile = open(devXPath, 'w')
        devYFile = open(devYPath, 'w')
        for point in test:
            date, Y, X = json.loads(point)
            devXFile.write(str(date) + '\t'+json.dumps(X) + '\n')
            devYFile.write(str(date) + '\t' + str(Y) + '\n')
        devXFile.close()
        devYFile.close()

        maxL1 = ''
        maxAccuracy = 0
        print stock
        for l1 in l1List:
            results = creg_driver.evaluate((trainXPath, trainYPath), (devXPath, devYPath), options={"--l1": l1})
            accuracy = round(float(sum(map(lambda v: 1 if v['true_label'] == v['predicted_label'] else 0, results.values()))) / len(results),4)
            if accuracy > maxAccuracy:
                maxL1 = l1
                maxAccuracy = accuracy 
            print accuracy,
        print maxAccuracy
        l1Dict[maxL1] += 1
       
print "recommend using l1 = ", max(l1Dict.iteritems(), key = operator.itemgetter(1))[0]

