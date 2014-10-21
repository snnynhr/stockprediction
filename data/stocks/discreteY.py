import json

stockjpath = 'stock.json'
stockjfile = open(stockjpath,"r+")
stockjson = json.load(stockjfile)

stockSet = set()

for date in stockjson:
	stockSet.update(stockjson[date]['endOfDayP'].keys())

stockD = dict()

for stock in stockSet:
	prev = None
	l = []
	for date in stockjson:
		if stock in stockjson[date]:
			if prev !=None:
				cur = stockjson[date][stock]
				if cur < prev:
					l.append((date, -1))
				else:
					l.append((date, 1))
				prev = cur
			else:
				prev = stockjson[date][stock]
