# author: Xiaote Zhu

import json
import sys

index = sys.argv[1]
print index


dictPath = '../data/dict/dict36761.json'
dictFile = open(dictPath, 'r')
dictList = json.load(dictFile)
word = dictList[int(index)]

print word

