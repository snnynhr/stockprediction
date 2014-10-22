# author: Xiaote Zhu

import os
import json

jfile = 'stock.json'
dirPath = 'sp08-10'

D = dict()
for f in os.listdir(dirPath):
	d = dict()
	if f.endswith('txt'):
		strf = open(dirPath+ '/' + f,"r")
		for line in strf:
			info = line.strip().split(",")
			if len(d) == 0:
				date=info[0]
				D[date] = d
			else:
				d[info[1]] = float(info[2])

open(jfile, 'w').write(json.dumps(D, sort_keys=True, indent = 2))

