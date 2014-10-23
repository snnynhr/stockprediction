import json
import os
import time

dowjones = "./sp500"
filename = "tickerStockTrain.json"
out = open(filename,'w')
for fname in os.listdir(dowjones):
	if fname.endswith('csv'):
		store = dict()
		f = open(dowjones+'/' + fname,'r+')
		l = f.readlines()
		for i in range(1, len(l)):
			p = l[i].split(",")
			date = p[0]
			price = p[-1][0:-2]
			dates = date.split("-")
			d = "".join(dates)
			store[d] = price
		out.write(fname[0:-4]+"\t"+json.dumps(store, sort_keys = True))
		out.write("\n")
		print "Converted " + fname
out.close()
