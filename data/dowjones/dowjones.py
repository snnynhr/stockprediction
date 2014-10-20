import json
import requests
import time
import os

stockjpath = '../stocks/stock.json'
stockjfile = open(stockjpath,"r+")
stockjson = json.load(stockjfile)

stockSet = set()

for date in stockjson:
	stockSet.update(stockjson[date]['endOfDayP'].keys())


count = 200000
for stock in stockSet:
	if os.path.isfile('./'+stock+'.json'):
		print stock+'.json exists already'
		continue
	print "fetching headlines of" + stock + "...",
	r = requests.get("http://betawebapi.dowjones.com/fintech/articles/api/v1/instrument/%s/?count=%d" %(stock.lower(),count))
	print r.status_code
	if r.status_code != 200:
		continue
	jfile = open(stock+'.json','w')
	jfile.write(json.dumps(r.json(), indent = 2))
	jfile.close()
	time.sleep(15)






	

