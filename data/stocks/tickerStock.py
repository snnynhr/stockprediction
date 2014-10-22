# author: Xiaote Zhu

import json

stockjpath = 'dayStock.json'
stockjfile = open(stockjpath,"r+")
stockjson = json.load(stockjfile)

stockSet = set()

for date in stockjson:
    stockSet.update(stockjson[date].keys())

stockList = sorted(stockSet)

jpath = 'tickerStock.json'
jfile = open(jpath, 'w')

for stock in stockList:
    print "reading %s ..." %stock
    d = dict()
    for date in stockjson:
        if stock in stockjson[date]:
            d[date] = stockjson[date][stock]
    jfile.write(stock + "\t" + json.dumps(d, sort_keys = True) + '\n')

jfile.close()
