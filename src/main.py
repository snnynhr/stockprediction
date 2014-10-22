# author: Xiaote Zhu

import Ylabel
import features
import json
import os
from sklearn import linear_model


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
        date = YList[0]
        Y.append(YList[1])
        if date in Xdict:
            X.append(Xdict[date])
        else:
            X.append([0] * dim)
    return X, Y


def main(stock, X, Y):
    return

Ypath = "../data/stocks/tickerStock.json"
Xdir = "../data/dowjones"
Yfile = open(Ypath,'r')
for line in Yfile:
    info = line.split('\t')
    if len(info) == 2:
        stock = info[0]
        print "building model for %s ..." %stock
        prices = json.loads(info[1])
        YList = Ylabel.discrete(prices)
        Xpath = Xdir + '/' + stock + '.json'
        if os.path.isfile(Xpath):
            print "extracting features ..."
            Xfile = open(Xpath, 'r')
            XD = json.load(Xfile)
            Xdict, dim = features.featureA(XD)
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

            X, Y = combine(Xdict, YList, dim)

            totalcount = len(Y)
            print "there are %d data points ..." % totalcount

            main(stock, X, Y)
        else:
            print "no headline file"
