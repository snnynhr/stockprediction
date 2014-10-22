# author: Xiaote Zhu

import json
import os
import time

dowjones = "../dowjones"

sumD = dict()

count = 0
for fname in os.listdir(dowjones):
	if fname.endswith('json'):
		jfile = open(dowjones+'/' + fname,'r+')
		d = json.load(jfile)
		headlines = d["Headlines"]
		sumD[fname[:-5]] = sumd = dict()
		sumd["count"] = count = len(headlines)
		if count > 0:
			sumd["start_time"] = headlines[0]["CreateTimestamp"]["Value"]
			sumd["end_time"] = headlines[-1]["CreateTimestamp"]["Value"]
			#sumd["start_time"] = time.strptime (headlines[0]["CreateTimestamp"]["Value"],"%Y-%m-%dT%H:%M:%S")
			#sumd["end_time"] = time.strptime (headlines[-1]["CreateTimestamp"]["Value"],"%Y-%m-%dT%H:%M:%S")
		jfile.close()
		count +=1
		if count%100:
			print "finished %d" % count


doSumFile = open('doSum.json','w')
doSumFile.write(json.dumps(sumD, sort_keys = True, indent = 2))
doSumFile.close()
