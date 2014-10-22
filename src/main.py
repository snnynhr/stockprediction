# author: Xiaote Zhu

import Ylabel
import features
import json
import os


def main(X, Y):
	return


Ypath = "../data/stocks/tickerStock.json"
Xdir = "../data/dowjones"
Yfile = open(Ypath,'r')
for line in Yfile:
	info = line.split('\t')
	if len(info) == 2:
		stock = info[0]
		prices = json.loads(info[1])
		Y = Ylabel.discrete(prices)
		Xpath = Xdir + '/' + stock + '.json'
		if os.path.isfile(Xpath):
			Xfile = open(Xpath, 'r')
			XD = json.load(Xfile)
			X = features.featureA(XD)
			print X
		break
