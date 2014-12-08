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
		# s1 = h["BodyHeadline"]
		# w1 = nltk.word_tokenize(s1)
		w2 = []
		if 'Abstract' in h.keys():
			if 'PARAGRAPH' in h['Abstract']['ABSTRACT'].keys():
				if '#text' in h['Abstract']['ABSTRACT']['PARAGRAPH'].keys():
					s2 = h['Abstract']['ABSTRACT']['PARAGRAPH']['#text']
					if type(s2) is unicode:
						w2.extend(nltk.word_tokenize(s2))
					elif type(s2) is list:
						for i in s2:
							w2.extend(nltk.word_tokenize(i))
		# words.extend(w1)
		words.extend(w2)
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
YpathT = "../data/training/dayStockTrain.json"
Xdir = "../data/dowjones"
inputDir = "../new_result/trainData3_sage"

if not os.path.exists(inputDir):
	os.makedirs(inputDir)

dictPath = '../data/dict/dict_lowered.json'
dictFile = codecs.open(dictPath, 'r', 'utf-8')
dictList = json.load(dictFile)
D = dict([(w[0], i) for i, w in enumerate(dictList)])


Yfile = codecs.open(Ypath, 'r', 'utf-8')
Ydict = json.load(Yfile)
YfileT = codecs.open(YpathT, 'r', 'utf-8')
YdictT = json.load(YfileT)
Ydict.update(YdictT)
total = len(Ydict)

# testNum = total /4
# trainNum = total - testNum
# testDays = Ydict.keys()[:testNum]
# trainDays = Ydict.keys()[testNum:]

testDays = []
trainDays = []
import random
random.seed(0)
for key in Ydict.keys():
	day = int(key[:6])
	if day >= 201401:
		r = random.randint(1, 10)
		if r > 7:
			testDays.append(key)
		else:
			trainDays.append(key)
	# if day >= 201408:
	# 	testDays.append(key)
	# elif day >= 201401:
	# 	trainDays.append(key)

testDays.sort()
trainDays.sort()

print "Number of training days" + str(len(trainDays))

countList = []
for Xfname in os.listdir(Xdir):
	if Xfname.endswith('.json'):
		Xfile = codecs.open('%s/%s' % (Xdir, Xfname), 'r', 'utf-8')
		Xdict = json.load(Xfile)
		featureD = dict()
		stock = Xfname[:-5]

		featureAMs(featureD, Xdict, stock)
		count = 0

		temp_list = []
		prevDay_p = None
		for i in xrange(0, len(trainDays)):
			day = trainDays[i]

			if stock in Ydict[day]:
				day_p = Ydict[day][stock]
			else:
				continue

			if prevDay_p is None:
				prevDay_p = day_p
				continue

			if day in featureD:
				count += 1
				if day_p >= prevDay_p:
					temp_list.append(('r_up', featureD[day]))
				else:
					temp_list.append(('r_down', featureD[day]))

			prevDay_p = day_p
		if count > 60:
			inputFile = codecs.open("%s/%s.txt" % (inputDir, stock), 'w', 'utf-8')
			for item in temp_list:
				tags = 'stock_%s %s' % (stock, item[0])
				words = " ".join(["%s:%d" % (key, value) for (key, value) in item[1].items()])
				if len(words) > 0:
					inputFile.write("%s\t%s\n" % (tags, words))
			inputFile.close()
		print stock, count
		countList.append(count)
		Xfile.close()

print "number of data for 100,150,200,250,300,350,400"
print len(filter(lambda x: x > 100, countList))
print len(filter(lambda x: x > 150, countList))
print len(filter(lambda x: x > 200, countList))
print len(filter(lambda x: x > 250, countList))
print len(filter(lambda x: x > 300, countList))
print len(filter(lambda x: x > 350, countList))
print len(filter(lambda x: x > 400, countList))
