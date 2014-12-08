# author: Xiaote Zhu

import codecs
import json
import os
import datetime
import nltk

testDir = "../new_result/testData3"
predDirs = ["../new_result/predictions_sage3"]
global r
global c

r = 0
c = 0
def evaluate(predDir,dataDict):
	global r, c
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
	r = r + correct_count
	c = c + pred_count
	return (correct_count/float(pred_count),money, correct_count, pred_count)

l = dict()

label = ['stock','expected_gain']
statD = dict()
for predDir in predDirs:
	statD[predDir] = ([],[])
	method = predDir.split('/')[-1].split('_')[-1]

	label.extend(['%s_accuracy' %method,'%s_gain' %method])
statD["expected_gain"] = []

print '\t'.join(label)

for fname in os.listdir(predDirs[0]):
	if fname.endswith('.txt'):
		stock = fname[:-4]
		dataFile = codecs.open('%s/%s' % (testDir, fname), 'r', 'utf-8')
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
			dataDict[day] = (float(prev_p), float(cur_p), true_l)
			end = float(cur_p)
		dataFile.close()
		summary = [stock, str(end / start)]
		statD['expected_gain'].append(end / start)
		for predDir in predDirs:
			accuracy, money, pc, cc = evaluate(predDir, dataDict)
			statD[predDir][0].append(accuracy)
			statD[predDir][1].append(money)
			l[stock] = (accuracy, cc)
			summary.extend([str(accuracy), str(money)])
		print "\t\t".join(summary)

import operator
sorted_x = sorted(l.items(), key=operator.itemgetter(1))
val = [i[1] for i in sorted_x]
print sum([i[0] for i in val]) / len(sorted_x)
print r / float(c)
print [i[0] + " " + str(i[1]) for i in sorted_x]

average = [str(sum(statD["expected_gain"]) / len(statD["expected_gain"]))]
for predDir in predDirs:
	aList,mList = statD[predDir]
	average.extend([str(sum(aList)/len(aList)),str(sum(mList)/len(mList))])

print "\t".join(average)
