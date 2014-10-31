# author: Xiaote Zhu

import nltk
import json
import time
import datetime

dictPath = '../data/dict/dict36761.json'
dictFile = open(dictPath, 'r')
dictList = json.load(dictFile)
D = dict([(w[0], i) for i, w in enumerate(dictList)])
dim = len(dictList)

# for sparse ones: featureD is a dictionary of dictionary
# headlines are all before 9:30 EST
def featureAMs(featureD, Xdict, Ylist, stock):
	headlines = Xdict["Headlines"]
	for h in headlines:
		sent = h["Headline"]
		words = nltk.word_tokenize(sent)
		c_time_str = h["CreateTimestamp"]["Value"]
		c_time = datetime.datetime.strptime(c_time_str, "%Y-%m-%dT%H:%M:%S")
		if c_time.hour >= 14 and c_time.minute >= 30:
			c_date_str = (c_time + datetime.timedelta(days=1)).strftime("%Y%m%d")
		else:
			c_date_str = c_time.strftime("%Y%m%d")
		if c_date_str not in Xdict:
			X[c_date_str] = dict()
		for w in words:
			if w in D:
				key = "%s_%d" % (stock,D[w])
				if key in X[c_date_str]:
					X[c_date_str][key] += 1
				else:
					X[c_date_str][key] = 1


# Ylabels from the previous states
def featureCs(featureD, Xdict, Ylist, stock, count = 5):
	for i in xrange(count, len(Ylist)):
		featureD[Ylist[i][0]] = dict(map(lambda x : ("%s_%d" %(stock, -x), Ylist[i-x][1]), xrange(1, count+1)))
