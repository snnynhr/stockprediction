# author: Xiaote Zhu

import codecs
import json
import os
import datetime
import nltk

# for sparse ones: featureD is a dictionary of dictionary
# headlines are all before 9:30 EST
def featureAMs(featureD, Xdict, stock):
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
		if c_date_str not in featureD:
			featureD[c_date_str] = dict()
		for w in words:
			if w in D:
				key = w
				if key in featureD[c_date_str]:
					featureD[c_date_str][key] += 1
				else:
					featureD[c_date_str][key] = 1

Ypath = "../data/stocks/dayStock.json"
Xdir = "../data/dowjones"
inputSageDir = "../new_result/trainData_sage"
inputRegXDir = "../new_result/trainData_reg+tempX"
inputRegYDir = "../new_result/trainData_regY_long"

dictPath = '../data/dict/dict_lowered.json'
dictFile = codecs.open(dictPath, 'r','utf-8')
dictList = json.load(dictFile)
D = dict([(w[0], i) for i, w in enumerate(dictList)])


Yfile = codecs.open(Ypath,'r','utf-8')
Ydict = json.load(Yfile)

testDays = []
trainDays = []

for key in Ydict.keys():
	if int(key[:6]) >= 201204:
		testDays.append(key) 
	else:
		trainDays.append(key)

testDays.sort()
trainDays.sort()

stocks = set()

for fname in os.listdir(inputSageDir):
	if fname.endswith('.txt'):
		s = fname[:-4]
		stocks.add(s)

print len(stocks)

temp_p = dict()
prevDict = dict()
for i in xrange(0,len(trainDays)):
	day = trainDays[i]
	prevDict[day] = dict()
	for stock in Ydict[day]:
		if stock not in temp_p:
			temp_p[stock] = Ydict[day][stock]
		elif Ydict[day][stock] > temp_p[stock]:
			prevDict[day][stock] = 1
		elif Ydict[day][stock] == temp_p[stock]:
			prevDict[day][stock] = 0
		else:
			prevDict[day][stock] = -1

for stock in stocks:
	Xfile = codecs.open('%s/%s.json' %(Xdir,stock),'r','utf-8')
	Xdict = json.load(Xfile)
	featureD = dict()

	featureAMs(featureD,Xdict,stock)
	count = 0

	prevDay_p = None
	#inputRegXFile = codecs.open('%s/%s.json' %(inputRegXDir,stock),'w','utf-8')
	inputRegYFile = codecs.open('%s/%s.txt' %(inputRegYDir,stock),'w','utf-8')
	for i in xrange(0,len(trainDays)):
		day = trainDays[i]

		if stock in Ydict[day]:
			day_p = Ydict[day][stock]
		else:
			print 'no more stock data for %s %s' %(stock,day)
			continue

		if prevDay_p == None:
			prevDay_p = day_p
			continue

		if day_p >= prevDay_p:
			change = 'r_up'
		else:
			change = 'r_down'

		# if day in featureD:
		# 	featureD[day].update(prevDict[day])
		# 	inputRegXFile.write('%s\t%s\n' %(day,json.dumps(featureD[day])))
		# else:
		# 	inputRegXFile.write('%s\t%s\n' %(day,json.dumps(prevDict[day])))
		inputRegYFile.write('%s\t%s\n' %(day,change))
		prevDay_p = day_p

	Xfile.close()
	#inputRegXFile.close()
	inputRegYFile.close()
	print stock