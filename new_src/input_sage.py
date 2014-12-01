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
inputDir = "../new_result/trainData_sage"

dictPath = '../data/dict/dict_lowered.json'
dictFile = codecs.open(dictPath, 'r','utf-8')
dictList = json.load(dictFile)
D = dict([(w[0], i) for i, w in enumerate(dictList)])


Yfile = codecs.open(Ypath,'r','utf-8')
Ydict = json.load(Yfile)

total = len(Ydict)

#testNum = total /4
#trainNum = total - testNum
#testDays = Ydict.keys()[:testNum]
#trainDays = Ydict.keys()[testNum:]

testDays = []
trainDays = []

for key in Ydict.keys():
	if int(key[:6]) >= 201204:
		testDays.append(key) 
	else:
		trainDays.append(key)

testDays.sort()
trainDays.sort()

print len(trainDays)

countList = []
for Xfname in os.listdir(Xdir):
	if Xfname.endswith('.json'):
		Xfile = codecs.open('%s/%s' %(Xdir,Xfname), 'r', 'utf-8')
		Xdict = json.load(Xfile)
		featureD = dict()
		stock = Xfname[:-5]

		featureAMs(featureD,Xdict,stock)
		count = 0

		temp_list = []
		prevDay_p = None
		for i in xrange(0,len(trainDays)):
			day = trainDays[i]

			if stock in Ydict[day]:
				day_p = Ydict[day][stock]
			else:
				continue

			if prevDay_p == None:
				prevDay_p = day_p
				continue

			if day in featureD:
				count += 1
				if day_p >= prevDay_p:
					temp_list.append(('r_up',featureD[day]))
				else:
					temp_list.append(('r_down',featureD[day]))
			
			prevDay_p = day_p
		if count > 400:
			inputFile = codecs.open("%s/%s.txt" %(inputDir,stock), 'w', 'utf-8')
			for item in temp_list:
				tags = 'stock_%s %s' %(stock, item[0])
				words = " ".join(["%s:%d" %(key,value) for (key,value) in item[1].items()])
				if len(words) > 0:
					inputFile.write("%s\t%s\n" %(tags, words))
			inputFile.close()
		print stock, count
		countList.append(count)
		Xfile.close()

print len(filter(lambda x : x> 100,countList))
print len(filter(lambda x : x> 150,countList))
print len(filter(lambda x : x> 200,countList))
print len(filter(lambda x : x> 250,countList))
print len(filter(lambda x : x> 300,countList))
print len(filter(lambda x : x> 350,countList))
print len(filter(lambda x : x> 400,countList))





