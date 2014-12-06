# author: Xiaote Zhu

import codecs
import json
import os
import datetime
import nltk

testDir = "../new_result/testData"
predDirs = ["../new_result/predictions_reg","../new_result/predictions_sage"]

def evaluate(predDir,dataDict):
	pred_count = 0
	correct_count = 0
	money = 1.0
	predFile = codecs.open('%s/%s' %(predDir,fname),'r','utf-8')
	for line in predFile:
		s, day, pred_l = line.strip().split('\t')
		prev_p, cur_p, true_l = dataDict[day]
		if pred_l == "none":
			continue
		else:
			pred_count += 1
			if pred_l == "up":
				money = money/prev_p * cur_p
				if true_l == "r_up":
					correct_count += 1
			elif pred_l == "down":
				if true_l == "r_down":
					correct_count += 1

	return (correct_count/float(pred_count),money)


for fname in os.listdir(predDirs[1]):
	if fname.endswith('.txt'):
		stock = fname[:-4]

		dataFile = codecs.open('%s/%s' %(testDir,fname),'r','utf-8')
		start = None
		end = None
		dataDict = dict()
		for line in dataFile:
			info = line.strip().split('\t')

			if len(info) == 0:
				continue
			elif len(info) == 5:
				s, day, prev_p, cur_p, true_l = info
			elif len(info) == 6:
				s, day, prev_p, cur_p, true_l, words = info

			if start is None:
				start = float(prev_p)
			dataDict[day] = (float(prev_p),float(cur_p),true_l)
			end = float(cur_p)
		dataFile.close()

		summary = [stock,str(end/start)]
		for predDir in predDirs:
			accuracy,money = evaluate(predDir,dataDict)
			summary.extend([str(accuracy),str(money)])

		print "\t\t".join(summary)

		#print "%s:%f accuracy for %d predictions, earn %f compared to %f" %(stock, (correct_count/float(pred_count)),pred_count,money, end/start)
