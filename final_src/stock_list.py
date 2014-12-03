import json
import codecs
import os

Ypath = "../data/stocks/tickerStock.json"
Yfile = codecs.open(Ypath,'r','utf-8')
Xdir = "../data/dowjones"

stockSet1 = set()
for line in Yfile:
	stock, prices = line.split('\t')
	temp_dict = json.loads(prices)
	n = len(temp_dict)
	if n > 1000:
		stockSet1.add(stock)

stockSet2 = set()
for fname in os.listdir(Xdir):
	if fname.endswith('.json'):
		stock = fname[:-5]
		stockSet2.add(stock)

print stockSet1 & stockSet2
print len(stockSet1 & stockSet2)
