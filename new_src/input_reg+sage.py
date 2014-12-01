# author: Xiaote Zhu

import codecs
import json
import os
import datetime
import nltk

# for sparse ones: featureD is a dictionary of dictionary
# headlines are all before 9:30 EST
def featureAMs(featureD, Xdict, stock, D):
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
inputRegXDir = "../new_result/trainData_reg+sageX"
inputRegYDir = "../new_result/trainData_regY"
weightPath = '../new_result/sage_result/weights300'
weightFile = codecs.open(weightPath,'r','utf-8')

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

wDict = dict()
for line in weightFile:
	tag, words = line.strip().split('\t', 1)
	wDict[tag]= set([s.split(':')[0] for s in words.split()])

for stock in stocks:
	print stock
	Xfile = codecs.open('%s/%s.json' %(Xdir,stock),'r','utf-8')
	Xdict = json.load(Xfile)
	featureD = dict()

	#print len(wDict['stock_%s' %stock])
	D = wDict['r_up']| wDict['r_down']| wDict['stock_%s' %stock] 
	#print len(D)
	featureAMs(featureD,Xdict,stock, D)
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

		if day in featureD and len(featureD[day]) > 0:
			if day_p >= prevDay_p:
				change = 'r_up'
			else:
				change = 'r_down'
			#inputRegXFile.write('%s\t%s\n' %(day,json.dumps(featureD[day])))
			inputRegYFile.write('%s\t%s\n' %(day,change))
		prevDay_p = day_p

	Xfile.close()
	#inputRegXFile.close()
	inputRegYFile.close()
	print stock