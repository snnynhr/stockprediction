# author: Xiaote Zhu
# stock price source: http://pages.swcp.com/stocks/

import os
import json

jfile = 'dayStock.json'
dirPath = 'sp08-10'

D = dict()
for f in os.listdir(dirPath):
	d = dict()
	if f.endswith('txt'):
		strf = open(dirPath+ '/' + f,"r")
		for line in strf:
			info = line.strip().split(",")
			date=info[0]
			if date not in D:
				D[date] = dict()
			else:
				D[date][info[1]] = float(info[5])

open(jfile, 'w').write(json.dumps(D, sort_keys=True, indent = 2))

