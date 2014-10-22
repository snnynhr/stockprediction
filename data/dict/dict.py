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
	map(countwords,words)


for fname in os.listdir(dowjones):
	if fname.endswith('json'):
		jfile = open(dowjones+'/' + fname,'r+')
		d = json.load(jfile)
		headlines = d["Headlines"]
		map(countHeadlines, headlines)
		jfile.close()


print len(wordD)
for word in wordD.keys():
  if wordD[word] < 5:
    del wordD[word]
print len(wordD)


sortedD = sorted(wordD.items(),key=(lambda (k,v):v), reverse = True)
dictFile = open('dict.json','w')
dictFile.write(json.dumps(sortedD))
dictFile.close()

