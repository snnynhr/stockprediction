# author: Xiaote Zhu

import codecs
import json
import os
import datetime
import nltk

weightDir = '../new_result/reg_result'
testDir = "../new_result/testData"
predictDir = "../new_result/predictions_reg"


def log_likelihood(words,d):
	result = d['_bias_']
	for w in words:
		if w in d:
			result += d[w] * words[w]
	return result 

for fname in os.listdir(testDir):
	if fname.endswith('txt'):
		print fname
		weightFile = codecs.open('%s/%s' %(weightDir,fname),'r','utf-8', errors='ignore')

		wDict = dict()
		weightFile.readline()

		second_line = weightFile.readline().strip().split(u'\t')
		wDict['_label_'] = second_line[0].split('_')[-1]
		wDict['_bias_'] = float(second_line[-1])

		for line in weightFile:
			label, word, weight = line.strip().split('\t')
			wDict[word] = float(weight)

		weightFile.close()

		dataFile = codecs.open('%s/%s' %(testDir,fname),'r','utf-8')
		predictFile = codecs.open('%s/%s' %(predictDir,fname),'w','utf-8')
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
				label_like = log_likelihood(words,wDict)

				if label_like > 0:
					result = wDict['_label_']
				else:
					if wDict['_label_'] == 'up':
						result = 'down'
					else:
						result = 'down'
			predictFile.write("%s\t%s\t%s\n" %(stock,day,result))

		predictFile.close()
		dataFile.close()











