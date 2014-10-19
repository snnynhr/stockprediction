import os
import json

jfile = 'stock.json'
dirPath = 'sp08-10'

D = dict()
for f in os.listdir(dirPath):
	d = dict()
	if f.endswith('txt'):
		strf = open(dirPath+ '/' + f,"r+")
		for line in strf:
			info = line.strip().split(",")
			if len(d) == 0:
				date=info[0]
				D[date] = d
				d['date']=dict()
				d['date']['year'] = int(date[:4])
				d['date']['month'] = int(date[4:6])
				d['date']['day'] = int(date[6:])
				d['endOfDayP'] = dict()
			else:
				d['endOfDayP'][info[1]] = float(info[2])

open(jfile, 'w').write(json.dumps(D, sort_keys=True, indent = 2))

