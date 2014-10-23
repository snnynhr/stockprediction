import json
import os

dowjones = "./sp500"
filename = "tickerStockTrain.json"
debug = "debug.txt"
out = open(filename, 'w')
debug = open(debug, 'w')
for fname in os.listdir(dowjones):
	if fname.endswith('csv'):
		store = dict()
		f = open(dowjones+'/' + fname, 'r+')
		l = f.readlines()
		if l[0].split(",")[0] != "Date":
			debug.write("No data for " + fname + "\n")
			continue
		for i in range(1, len(l)):
			p = l[i].split(",")
			date = p[0]
			price = p[-1][0:-2]
			dates = date.split("-")
			d = "".join(dates)
			store[d] = price
		out.write(fname[0:-4]+"\t"+json.dumps(store, sort_keys=True))
		out.write("\n")
		debug.write("Converted " + fname + "\n")
out.close()
debug.close()
