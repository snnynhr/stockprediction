# author: Xiaote Zhu

import nltk
import json
import time

dictPath = '../data/dict/dict36761.json'
dictFile = open(dictPath, 'r')
dictList = json.load(dictFile)
D = dict([(w[0],i) for i,w in enumerate(dictList)])
dim = len(dictList)


def featureA(XD):
	headlines = XD["Headlines"]
	print headlines
	X = dict()
	for h in headlines:
		sent = h["Headline"]
		words = nltk.word_tokenize(sent)
		c_time_str = h["CreateTimestamp"]["Value"]
		c_time = time.strptime (c_time_str,"%Y-%m-%dT%H:%M:%S")
		c_date_str = time.strftime("%Y%m%d",c_time)
		if c_date_str not in X:
			X = [0] * dim
		for w in words:
			if w in D:
				X[D[w]] += 1
	return X
