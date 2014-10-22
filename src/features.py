# author: Xiaote Zhu

import nltk
import json
import time

dictPath = '../data/dict/dict36761.json'
dictFile = open(dictPath, 'r')
dictList = json.load(dictFile)
dim = len(dictList)


def featureA(XD):
	headlines = D["Headlines"]
	X = dict()
	for h in headlines:
		sent = h["Headline"]
		words = nltk.word_tokenize(sent)
		c_time_str = h["CreateTimestamp"]["Value"]
		c_time = time.strptime (c_time_str,"%Y-%m-%dT%H:%M:%S")
		c_date_str = c_time
