# author: Xiaote Zhu
import Ylabel
import features 
import json
import os
import copy

# change here for new folders
XYdir = "../XYdata/5/full"
Ypath = "../data/stocks/tickerStock.json"
Xdir = "../data/dowjones"

if not os.path.exists(XYdir):
    os.mkdir(XYdir)
# change here too
readmePath = XYdir + '/README.md'

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

# destructively modify D1
def mergeFeatures(D1, D2):
    for key in D2:
        if key in D1:
            D1[key].update(D2[key])
        else:
            D1[key] = D2[key]

def crossMarketFeatures(stockList,fnList1, Ylists):
    featureD = dict()
    for i in xrange(len(stockList)):
        stock = stockList[i]
        Ylist = Ylist[i]
        Xpath = Xdir + '/' + stock + '.json'
        if os.path.isfile(Xpath):
            Xfile = open(Xpath, 'r')
            Xdict = json.load(Xfile)
            for fn in fnList1:
                print "including %s from %s ..." %(str(fn),stock)
                features.fn(featureD, Xdict, Ylist, stock)
    return featureD

def singleStockFeature(stock, fnList2, Ylist):
    featureD = dict()
    Xpath = Xdir + '/' + stock + '.json'
    if os.path.isfile(Xpath):
        Xfile = open(Xpath, 'r')
        Xdict = json.load(Xfile)
        for fn in fnList2:
            print "including %s for %s ..." %(str(fn),stock)
            features.fn(featureD, Xdict, Ylist, stock)
        return featureD
    else:
        return None

# fnList1 for features that are specfic to a stock
# fnList2 for features that are the same to all stocks
def main(fnList1,fnList2, overWriting = True):
    print "extracting features ..."

    Yfile = open(Ypath,'r')
    stockList = []
    Ylists = []
    for line in Yfile:
        info = line.split('\t')
        if len(info) ==2:
            stockList.append(info[0])
            prices = json.loads(info[1])
            Ylists.append(Ylabel.discrete(prices))
    Yfile.close()
    
    fnNames = map(str, fnList1 + fnList2)
    readmeContent = '+'.join(fnNames)
    if not os.path.isfile(readmePath):
        readmefile = open(readmePath, 'w')
        readmefile.write(readmeContent)
        readmefile.close()

    featureDGeneral = crossMarketFeatures(stockList,fnList1, YLists)

    for i in xrange(len(stockList)):
        stock = stockList[i]
        Ylist = YLists[i]
        print "building XYfile for %s ..." %stock
        featureD = singleStockFeature(stock, fnList2, Ylist)
        if featureD == None:
            print "no headline file"
            continue
        mergeFeatures(featureD, featureDGeneral)

        start_Y = Ylist[0][0]
        end_Y = Ylist[-1][0]
        start_X = min(featureD.keys())
        end_X = max(featureD.keys())

        #caution: X and Y have to use the format of %Y%m%d
        start_date = max(start_X, start_Y)
        end_date = min(end_X, end_Y)

        if start_date>= end_date:
            print "not enough data"
            continue

        print "time range of data: %s - %s" %(start_date, end_date)

        featureD = pruneX(featureD, start_date, end_date)
        Ylist = pruneY(Ylist, start_date, end_date)

        X, Y, date = combineS(featureD, Ylist)

        totalcount = len(Y)
        print "there are %d data points ..." % totalcount

        XYPath = XYdir + '/' + stock + '.json'

        if totalcount < 1000:
            print "not enough data points"
            if os.path.isfile(XYPath):
                os.remove(XYPath)
                print  "remove %s" %(XYPath)
            continue

        if not overWriting and os.path.isfile(XYPath):
            print "file already exists"
            continue
        
        else:
            XYfile = open(XYPath, 'w')
            print "creating new files..."
            for i in xrange(totalcount):
                XYfile.write(json.dumps((Date[i],Y[i],X[i])) + '\n')
            XYfile.close()


