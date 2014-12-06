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


inputPath = "../new_result/train.txt"
outputDir = "../new_result/testData"

dictPath = '../data/dict/dict_lowered.json'
dictFile = codecs.open(dictPath, 'r', 'utf-8')
dictList = json.load(dictFile)
D = dict([(w[0], i) for i, w in enumerate(dictList)])

Ypath = "../data/stocks/dayStock.json"
YpathT = "../data/training/dayStockTrain.json"
Xdir = "../data/dowjones"
inputDir = "../new_result/trainData_sage"

Yfile = codecs.open(Ypath, 'r', 'utf-8')
Ydict = json.load(Yfile)
YfileT = codecs.open(YpathT, 'r', 'utf-8')
YdictT = json.load(YfileT)
Ydict.update(YdictT)
total = len(Ydict)


testDays = []
trainDays = []

for key in Ydict.keys():
	day = int(key[:6])
	if day >= 201405:
		testDays.append(key)
	elif day >= 201401:
		trainDays.append(key)

testDays.sort()
trainDays.sort()

print len(testDays)

inputFile = codecs.open(inputPath, 'r', 'utf-8')
stocks = set()

for line in inputFile:
	s = (line.split()[0]).split('_')[1]
	stocks.add(s)

print len(stocks)

inputFile.close()

countList = []
for stock in stocks:
	Xfile = codecs.open('%s/%s.json' % (Xdir, stock), 'r', 'utf-8')
	Xdict = json.load(Xfile)
	featureD = dict()

	featureAMs(featureD, Xdict, stock)
	count = 0

	temp_list = []
	prevDay_p = Ydict[trainDays[-1]][stock]
	for i in xrange(0, len(testDays)):
		day = testDays[i]

		if s in Ydict[day]:
			day_p = Ydict[day][stock]
		else:
			print 'no more stock data for %s' % stock
			continue

		if day_p >= prevDay_p:
			change = 'r_up'
		else:
			change = 'r_down'

		if day in featureD:
			count += 1
			words = featureD[day]
		else:
			words = dict()

		temp_list.append((stock, str(day), str(prevDay_p), str(day_p), change, words))
		prevDay_p = day_p

	outputFile = codecs.open('%s/%s.txt' % (outputDir, stock), 'w', 'utf-8')
	for item in temp_list:
		tags = "\t".join(item[:-1])
		words = " ".join(["%s:%d" % (key, value) for (key, value) in item[-1].items()])

		outputFile.write("%s\t%s\n" % (tags, words))

	outputFile.close()
	Xfile.close()
	countList.append(count)
	print stock, count


print len(filter(lambda x: x > 100, countList))
print len(filter(lambda x: x > 150, countList))
print len(filter(lambda x: x > 200, countList))
print len(filter(lambda x: x > 250, countList))
print len(filter(lambda x: x > 300, countList))
print len(filter(lambda x: x > 350, countList))
print len(filter(lambda x: x > 400, countList))
