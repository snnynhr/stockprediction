# author: Xiaote Zhu
import Ylabel
import features
import json
import os
from sklearn import linear_model
import copy


def pruneX(Xdict, start, end):
    for date in Xdict.keys():
        if date > end or date < start:
            del Xdict[date]
    return Xdict

# YList sorted
def pruneY(YList, start, end):
    num = len(YList)
    s_index = None
    e_index = None
    for i in xrange(num):
        if s_index != None and YList[i] >= start:
            s_index = i
        elif e_index != None and YList[num-i -1] <= end:
            e_index = num-i
        if s_index != None and e_index != None:
            return YList[s_index: e_index]
    return YList[s_index: e_index]  

def combine(Xdict, YList, dim):
    X = []
    Y = []
    for item in YList:
        date = item[0]
        Y.append(item[1])
        if date in Xdict:
            X.append(Xdict[date])
        else:
            X.append([0] * dim)
    return X, Y

def combineS(Xdict, YList):
    X = []
    Y = []
    D = []
    for item in YList:
        date = item[0]
        D.append(date)
        Y.append(item[1])
        if date in Xdict:
            X.append(Xdict[date])
        else:
            X.append(dict())
    return X, Y, D

# change here for new folders
XYdir = "../XYdata/2/full"
Ypath = "../data/stocks/tickerStock.json"
Xdir = "../data/dowjones"
Yfile = open(Ypath,'r')

# change here too
readmePath = XYdir + '/README.md'

# write documentation in md format
readmeContent = \
"""
featuresBs + discrete
"""

if not os.path.isfile(readmePath):
    readmefile = open(readmePath, 'w')
    readmefile.write(readmeContent)
    readmefile.close()

def mainA():
    for line in Yfile:
        info = line.split('\t')
        if len(info) == 2:
            stock = info[0]
            print "building XYfile for %s ..." %stock
            prices = json.loads(info[1])
            YList = Ylabel.discrete(prices)
            Xpath = Xdir + '/' + stock + '.json'
            if os.path.isfile(Xpath):
                print "extracting features ..."
                Xfile = open(Xpath, 'r')
                XD = json.load(Xfile)
                Xdict, dim = features.featureAs(XD)
                # for date in X:
                #     s = sum(X[date])
                #     if s != 0 :
                #         print date, s
                if len(Xdict) < 1:
                    print "no headline data"
                    continue

                start_Y = YList[0][0]
                end_Y = YList[-1][0]
                start_X = min(Xdict.keys())
                end_X = max(Xdict.keys())
                print "time range of stock prices: %s - %s" %(start_Y, end_Y)
                print "time range of headlines: %s - %s" %(start_X, end_X)
                #caution: X and Y have to use the format of %Y%m%d
                start_date = max(start_X, start_Y)
                end_date = min(end_X, end_Y)

                if start_date>= end_date:
                    print "not enough data"
                    continue

                print "time range of data: %s - %s" %(start_date, end_date)
                
                Xdict = pruneX(Xdict, start_date, end_date)
                YList = pruneY(YList, start_date, end_date)

                X, Y, Date = combineS(Xdict, YList, dim)

                #print [sum(x) for x in X]
                #print Y
                totalcount = len(Y)
                print "there are %d data points ..." % totalcount

                XYPath = XYdir + '/' + stock + '.json'
                XYfile = open(XYPath, 'w')
                for i in xrange(totalcount):
                    XYfile.write(json.dumps((Date[i],Y[i],X[i])) + '\n')
                XYfile.close()

            else:
                print "no headline file"

def mainB():
    print "extracting features ..."
    featureD = dict()
    for line in Yfile:
        info = line.split('\t')
        if len(info) == 2:
            stock = info[0]
            Xpath = Xdir + '/' + stock + '.json'
            if os.path.isfile(Xpath):
                print "including headlines from %s ..." %stock
                Xfile = open(Xpath, 'r')
                XD = json.load(Xfile)
                features.featureBs(featureD,XD,stock)
                # for date in X:
                #     s = sum(X[date])
                #     if s != 0 :
                #         print date, s
        break


    for line in Yfile:
        info = line.split('\t')
        Xdict = copy.deepcopy(featureD)
        if len(info) == 2:
            stock = info[0]

            print "building XYfile for %s ..." %stock
            prices = json.loads(info[1])
            YList = Ylabel.discrete(prices)

            start_Y = YList[0][0]
            end_Y = YList[-1][0]
            start_X = min(Xdict.keys())
            end_X = max(Xdict.keys())
            print "time range of stock prices: %s - %s" %(start_Y, end_Y)
            print "time range of headlines: %s - %s" %(start_X, end_X)
            #caution: X and Y have to use the format of %Y%m%d
            start_date = max(start_X, start_Y)
            end_date = min(end_X, end_Y)

            if start_date>= end_date:
                print "not enough data"
                continue

            print "time range of data: %s - %s" %(start_date, end_date)
            
            Xdict = pruneX(Xdict, start_date, end_date)
            YList = pruneY(YList, start_date, end_date)

            X, Y, Date = combineS(Xdict, YList)

            #print [sum(x) for x in X]
            #print Y
            totalcount = len(Y)
            print "there are %d data points ..." % totalcount

            XYPath = XYdir + '/' + stock + '.json'
            XYfile = open(XYPath, 'w')
            for i in xrange(totalcount):
                XYfile.write(json.dumps((Date[i],Y[i],X[i])) + '\n')
            XYfile.close()
mainB()