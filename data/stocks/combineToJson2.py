# author: Xiaote Zhu

import json
import time

csvpath = "SPDaily.062313.csv"
csvfile = open(csvpath,"r")
jpath = "stock.json"
jfile = open(jpath, "r")

D = json.load(jfile)
count = 0
for line in csvfile:
	info = line.strip().split('\t')
	if count == 0:
		columns = info
		for i in xrange(len(columns)):
			if columns[i]=='year' or columns[i] =='month' or columns[i] == 'day':
				pass
			elif columns[i].startswith('P_'):
				columns[i] = columns[i][2:]
			else:
				columnLength = i
				break
		columns = columns[:columnLength]
		if len(columns)>=3:
			count += 1
	else:
		date = time.strftime('%Y%m%d',(info[0], info[1], info[2]))
# 		priceD = dict(zip(columns[3:columnLength], map(float,info[3:columnLength])))
		priceD = dict(map(lambda (t, p): (t, float(p)), filter(lambda (t, p): p, zip(columns[3:columnLength], info[3:columnLength]))))
		if date not in D:
			D[date] = priceD
		elif date in D:
			# for key in priceD:
			#  	if key in D[date]['endOfDayP'] and D[date]['endOfDayP'][key] - priceD[key] > 1:
			#  		print D[date]['endOfDayP'][key],  priceD[key]
			D[date].update(priceD)


jfile.close()

open(jpath, 'w').write(json.dumps(D, sort_keys=True, indent = 2))


