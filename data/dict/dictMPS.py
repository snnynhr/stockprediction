# author: Xiaote Zhu

import json
import os
import nltk
import multiprocessing
from multiprocessing import Process
import sys

dowjones = "../dowjones"
prefix = "stockdicts"
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

def countwordsP(w, D):
	print type(D)
	if w not in D:
		D[w] = 0
	D[w] += 1

def countwordsNP(l, D):
	for w in l:
		if w not in D:
			D[w] = 0
		D[w] += 1

def countHeadlinesP(h, fD):
	sent = h["Headline"]
	words = nltk.word_tokenize(sent)
	countwordsNP(words, fD)
	s1 = h["BodyHeadline"]
	w1 = nltk.word_tokenize(s1)
	countwordsNP(words, fD)
	if 'Abstract' in h.keys():
		if 'PARAGRAPH' in h['Abstract']['ABSTRACT'].keys():
			if '#text' in h['Abstract']['ABSTRACT']['PARAGRAPH'].keys():
				s2 = h['Abstract']['ABSTRACT']['PARAGRAPH']['#text']
				if type(s2) is unicode:
					w2 = nltk.word_tokenize(s2)
					countwordsNP(words, fD)
				elif type(s2) is list:
					for i in s2:
						w2 = nltk.word_tokenize(i)
						countwordsNP(words, fD)

def load(fname):
	jfile = open(dowjones + '/' + fname, 'r+')
	d = json.load(jfile)
	headlines = d["Headlines"]
	fD = dict()
	for i in headlines:
		countHeadlinesP(i, fD)
	sD = sorted(fD.items(), key=(lambda (k, v): v), reverse = True)
	dFile = open(prefix + '/dict' + fname, 'w')
	dFile.write(json.dumps(sD))
	dFile.close()
	jfile.close()

MAXNUM = 16
processes = []
fns = []
CURR = 0
MAX = 618
c = 0
if __name__ == '__main__':
	multiprocessing.freeze_support()
	for fname in os.listdir(dowjones):
		if fname.endswith('json') and c < MAX:
			c = c + 1
			if (CURR < MAXNUM):
				fns[len(fns):] = [fname]
				CURR = CURR + 1
			else:
				CURR = 1
				for i in xrange(0, MAXNUM):
					print "Processing " + fns[i]
					p = Process(target=load, args=(fns[i],))
					processes[i:] = [p]
				for i in xrange(0, MAXNUM):
					processes[i].start()
				for i in xrange(0, MAXNUM):
					processes[i].join()
				print "DONE"
				fns = [fname]
		elif c <= MAX:
			c = c + 1
			l = len(fns)
			for i in xrange(0, l):
				print "Processing " + fns[i]
				p = Process(target=load, args=(fns[i],))
				processes[i:] = [p]
			for i in xrange(0, l):
				processes[i].start()
			for i in xrange(0, l):
				processes[i].join()
			print "DONE"
