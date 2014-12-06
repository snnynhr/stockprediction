import json
import os

dowjones = "./sp500"
filename = "dayStockTrain.json"
debug = "debugS.txt"
out = open(filename, 'w')
debug = open(debug, 'w')

main = dict()
for fname in os.listdir(dowjones):
	if fname.endswith('csv'):
		f = open(dowjones+'/' + fname, 'r+')
		l = f.readlines()
		stock = fname[0:-4]
		if l[0].split(",")[0] != "Date":
			debug.write("No data for " + fname + "\n")
			continue
		for i in range(1, len(l)):
			p = l[i].split(",")
			date = p[0]
			price = p[-1][0:-2]
			dates = date.split("-")
			d = "".join(dates)
			if d not in main.keys():
				main[d] = dict()
			main[d][stock] = float(price)

out.write(json.dumps(main, sort_keys=True, indent=2))
out.write("\n")
out.close()
debug.close()
