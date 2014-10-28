# author: Xiaote Zhu

import json
import os
import nltk

dowjones = "../dowjones"

wordD = dict()

def countwords(w):
	if w not in wordD:
		wordD[w] = 0
	wordD[w] += 1

def countHeadlines(h):
	sent = h["Headline"]
	words = nltk.word_tokenize(sent)
	map(countwords, words)
	s1 = h["BodyHeadline"]
	w1 = nltk.word_tokenize(s1)
	map(countwords, w1)
	if 'Abstract' in h.keys():
		if 'PARAGRAPH' in h['Abstract']['ABSTRACT'].keys():
			if '#text' in h['Abstract']['ABSTRACT']['PARAGRAPH'].keys():
				s2 = h['Abstract']['ABSTRACT']['PARAGRAPH']['#text']
				if type(s2) is unicode:
					w2 = nltk.word_tokenize(s2)
					map(countwords, w2)
				elif type(s2) is list:
					for i in s2:
						w2 = nltk.word_tokenize(i)
						map(countwords, w2)

for fname in os.listdir(dowjones):
	if fname.endswith('json'):
		jfile = open(dowjones + '/' + fname, 'r+')
		print "Processing " + fname
		d = json.load(jfile)
		headlines = d["Headlines"]
		map(countHeadlines, headlines)
		jfile.close()


print len(wordD)
for word in wordD.keys():
	if wordD[word] < 5:
		del wordD[word]
print len(wordD)

sortedD = sorted(wordD.items(), key=(lambda (k, v): v), reverse = True)
dictFile = open('dict' + str(len(sortedD) + '.json'), 'w')
dictFile.write(json.dumps(sortedD))
dictFile.close()
