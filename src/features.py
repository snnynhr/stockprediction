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

# for dense feature vectors: X is a dictionary of list
def featureA(XD):
	headlines = XD["Headlines"]
	X = dict()
	for h in headlines:
		sent = h["Headline"]
		words = nltk.word_tokenize(sent)
		c_time_str = h["CreateTimestamp"]["Value"]
		c_time = time.strptime(c_time_str, "%Y-%m-%dT%H:%M:%S")
		c_date_str = time.strftime("%Y%m%d", c_time)
		if c_date_str not in X:
			X[c_date_str] = [0] * dim
		for w in words:
			if w in D:
				X[c_date_str][D[w]] += 1
	return X, dim

# for sparse ones: X is a dictionary of dictionary
def featureAs(XD, extra=''):
	headlines = XD["Headlines"]
	X = dict()
	for h in headlines:
		sent = h["Headline"]
		words = nltk.word_tokenize(sent)
		c_time_str = h["CreateTimestamp"]["Value"]
		c_time = time.strptime(c_time_str, "%Y-%m-%dT%H:%M:%S")
		c_date_str = time.strftime("%Y%m%d", c_time)
		if c_date_str not in X:
			X[c_date_str] = dict()
		for w in words:
			if w in D:
				key = str(D[w]) + extra
				if key in X[c_date_str]:
					X[c_date_str][key] += 1
				else:
					X[c_date_str][key] = 1
	return X, dim

# for sparse ones: X is a dictionary of dictionary
def featureAMs(XD, extra=''):
	headlines = XD["Headlines"]
	X = dict()
	for h in headlines:
		sent = h["Headline"]
		words = nltk.word_tokenize(sent)
		c_time_str = h["CreateTimestamp"]["Value"]
		c_time = datetime.strptime(c_time_str, "%Y-%m-%dT%H:%M:%S")
		if c_time.hour >= 14 and c_time.minute >= 30:
			c_date_str = datetime.strftime("%Y%m%d", c_time + datetime.timedelta(days=1))
		else:
			c_date_str = datetime.strftime("%Y%m%d", c_time)
		if c_date_str not in X:
			X[c_date_str] = dict()
		for w in words:
			if w in D:
				key = str(D[w]) + extra
				if key in X[c_date_str]:
					X[c_date_str][key] += 1
				else:
					X[c_date_str][key] = 1
	return X, dim

# headlines from all stocks
def featureBs(featureD, XD, stock):
	X, dim = featureAs(XD, stock)
	if len(X) < 1:
		print "not enough headlines"
		return
	for key in X:
		if key in featureD:
			featureD[key].update(X[key])
		else:
			featureD[key] = X[key]

# headlines from all stocks  (before 9:30 EST)
def featureBMs(featureD, XD, stock):
	X, dim = featureAMs(XD, stock)
	if len(X) < 1:
		print "not enough headlines"
		return
	for key in X:
		if key in featureD:
			featureD[key].update(X[key])
		else:
			featureD[key] = X[key]

# Ylabels from the previous states
def featureCs(Ylist, count = 3):
	featureD = dict()
	for i in xrange(count, len(Ylist)):
		featureD[Ylist[i][0]] = dict(map(lambda x : (-x, Ylist[i-x][1]), xrange(1, count+1)))
	return featureD
