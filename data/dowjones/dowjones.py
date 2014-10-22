# author: Xiaote Zhu

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


#count = 200000
#count = 100000
#count = 5000
for stock in stockSet:
	if os.path.isfile('./'+stock+'.json'):
		print stock+'.json exists already'
		continue
	r = requests.get("http://betawebapi.dowjones.com/fintech/articles/api/v1/instrument/%s/?count=1")
	if r.status_code != 200:
		pass
	else:
		o = r.json()
		if len(o["Headlines"]) == 0:
			print "Headlines do not exist for" + stock
			continue
	count = 200000
	print "fetching headlines of" + stock + "..."
	while count > 1:
		count /= 2
		r = requests.get("http://betawebapi.dowjones.com/fintech/articles/api/v1/instrument/%s/?count=%d" %(stock.lower(),count))
		if r.status_code != 200:
			if count == 1:
				print stock, r.status_code
			time.sleep(10)
			continue
		o = r.json()
		if len(o["Headlines"]) > 0:
			print stock + " with " + str(count)
			break
		time.sleep(10)
	jfile = open(stock+'.json','w')
	jfile.write(json.dumps(o, indent = 2))
	jfile.close()
	time.sleep(10)






	

