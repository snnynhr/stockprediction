# author: Xiaote Zhu

import codecs
import json
import os
import datetime
import nltk
import sys
weightPath = '../new_result/sage_result/weights'+sys.argv[1]
weightFile = codecs.open(weightPath,'r','utf-8')
testDir = "../new_result/testData"
predictDir = "../new_result/predictions_sage"


def log_likelihood(words, d):
	result = 0
	for w in words:
		if w in d:
			result += d[w] * words[w]
	return result

for line in weightFile:
	tag, words = line.strip().split('\t', 1)
	if tag == 'r_up':
		up_dict = dict([(s.split(':')[0], float(s.split(':')[1])) for s in words.split()])
	elif tag == 'r_down':
		down_dict = dict([(s.split(':')[0], float(s.split(':')[1])) for s in words.split()])

weightFile.close()

for fname in os.listdir(testDir):
	dataFile = codecs.open('%s/%s' % (testDir, fname), 'r', 'utf-8')
	predictFile = codecs.open('%s/%s' % (predictDir, fname), 'w', 'utf-8')
	stock = fname[:-4]
	for line in dataFile:
		if line.strip() == '':
			continue
		info = line.split('\t')
		day = info[1]
		words = dict([(s.split(':')[0], int(s.split(':')[1])) for s in info[-1].split()])
		if len(words) == 0:
			result = "none"
		else:
			up_like = log_likelihood(words,up_dict)
			down_like = log_likelihood(words,down_dict)

			if up_like > down_like:
				result = "up"
			else:
				result = "down"
		predictFile.write("%s\t%s\t%s\n" %(stock,day,result))

	predictFile.close()
	dataFile.close()
