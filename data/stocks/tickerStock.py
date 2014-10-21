import json

stockjpath = '../stocks/stock.json'
stockjfile = open(stockjpath,"r+")
stockjson = json.load(stockjfile)

stockSet = set()

for date in stockjson:
	stockSet.update(stockjson[date]['endOfDayP'].keys())

stockD = dict()

for stock in stockSet:
	stockD[stock] = l = []
	for date in stockjson:
		if stock in stockjson[date]:
			l.append((date, stock[date][stock]))