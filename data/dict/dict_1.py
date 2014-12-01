# author: Xiaote Zhu

import json
import os
import nltk
import codecs

dowjones = "../dowjones"

punct = {u"\u0021", u"\u0022", u"\u0023", u"\u0025", u"\u0026", u"\u0027", u"\u0028",
u"\u0029", u"\u002a", u"\u002c", u"\u002d", u"\u002e", u"\u002f", u"\u003a", u"\u003b",
u"\u003f", u"\u0040", u"\u005b", u"\u005c", u"\u005d", u"\u005f", u"\u007b", u"\u007d",
u"\u00a1", u"\u00ab", u"\u00b7", u"\u00bb", u"\u00bf", u"\u037e", u"\u0387", u"\u055a",
u"\u055b", u"\u055c", u"\u055d", u"\u055e", u"\u055f", u"\u0589", u"\u058a", u"\u05be",
u"\u05c0", u"\u05c3", u"\u05c6", u"\u05f3", u"\u05f4", u"\u0609", u"\u060a", u"\u060c",
u"\u060d", u"\u061b", u"\u061e", u"\u061f", u"\u066a", u"\u066b", u"\u066c", u"\u066d",
u"\u06d4", u"\u0700", u"\u0701", u"\u0702", u"\u0703", u"\u0704", u"\u0705", u"\u0706",
u"\u0707", u"\u0708", u"\u0709", u"\u070a", u"\u070b", u"\u070c", u"\u070d", u"\u07f7",
u"\u07f8", u"\u07f9", u"\u0830", u"\u0831", u"\u0832", u"\u0833", u"\u0834", u"\u0835",
u"\u0836", u"\u0837", u"\u0838", u"\u0839", u"\u083a", u"\u083b", u"\u083c", u"\u083d",
u"\u083e", u"\u0964", u"\u0965", u"\u0970", u"\u0df4", u"\u0e4f", u"\u0e5a", u"\u0e5b",
u"\u0f04", u"\u0f05", u"\u0f06", u"\u0f07", u"\u0f08", u"\u0f09", u"\u0f0a", u"\u0f0b",
u"\u0f0c", u"\u0f0d", u"\u0f0e", u"\u0f0f", u"\u0f10", u"\u0f11", u"\u0f12", u"\u0f3a",
u"\u0f3b", u"\u0f3c", u"\u0f3d", u"\u0f85", u"\u0fd0", u"\u0fd1", u"\u0fd2", u"\u0fd3",
u"\u0fd4", u"\u104a", u"\u104b", u"\u104c", u"\u104d", u"\u104e", u"\u104f", u"\u10fb",
u"\u1361", u"\u1362", u"\u1363", u"\u1364", u"\u1365", u"\u1366", u"\u1367", u"\u1368",
u"\u1400", u"\u166d", u"\u166e", u"\u169b", u"\u169c", u"\u16eb", u"\u16ec", u"\u16ed",
u"\u1735", u"\u1736", u"\u17d4", u"\u17d5", u"\u17d6", u"\u17d8", u"\u17d9", u"\u17da",
u"\u1800", u"\u1801", u"\u1802", u"\u1803", u"\u1804", u"\u1805", u"\u1806", u"\u1807",
u"\u1808", u"\u1809", u"\u180a", u"\u1944", u"\u1945", u"\u19de", u"\u19df", u"\u1a1e",
u"\u1a1f", u"\u1aa0", u"\u1aa1", u"\u1aa2", u"\u1aa3", u"\u1aa4", u"\u1aa5", u"\u1aa6",
u"\u1aa8", u"\u1aa9", u"\u1aaa", u"\u1aab", u"\u1aac", u"\u1aad", u"\u1b5a", u"\u1b5b",
u"\u1b5c", u"\u1b5d", u"\u1b5e", u"\u1b5f", u"\u1b60", u"\u1c3b", u"\u1c3c", u"\u1c3d",
u"\u1c3e", u"\u1c3f", u"\u1c7e", u"\u1c7f", u"\u1cd3", u"\u2010", u"\u2011", u"\u2012",
u"\u2013", u"\u2014", u"\u2015", u"\u2016", u"\u2017", u"\u2018", u"\u2019", u"\u201a",
u"\u201b", u"\u201c", u"\u201d", u"\u201e", u"\u201f", u"\u2020", u"\u2021", u"\u2022",
u"\u2023", u"\u2024", u"\u2025", u"\u2026", u"\u2027", u"\u2030", u"\u2031", u"\u2032",
u"\u2033", u"\u2034", u"\u2035", u"\u2036", u"\u2037", u"\u2038", u"\u2039", u"\u203a",
u"\u203b", u"\u203c", u"\u203d", u"\u203e", u"\u203f", u"\u2040", u"\u2041", u"\u2042",
u"\u2043", u"\u2045", u"\u2046", u"\u2047", u"\u2048", u"\u2049", u"\u204a", u"\u204b",
u"\u204c", u"\u204d", u"\u204e", u"\u204f", u"\u2050", u"\u2051", u"\u2053", u"\u2054",
u"\u2055", u"\u2056", u"\u2057", u"\u2058", u"\u2059", u"\u205a", u"\u205b", u"\u205c",
u"\u205d", u"\u205e", u"\u207d", u"\u207e", u"\u208d", u"\u208e", u"\u2329", u"\u232a",
u"\u2768", u"\u2769", u"\u276a", u"\u276b", u"\u276c", u"\u276d", u"\u276e", u"\u276f",
u"\u2770", u"\u2771", u"\u2772", u"\u2773", u"\u2774", u"\u2775", u"\u27c5", u"\u27c6",
u"\u27e6", u"\u27e7", u"\u27e8", u"\u27e9", u"\u27ea", u"\u27eb", u"\u27ec", u"\u27ed",
u"\u27ee", u"\u27ef", u"\u2983", u"\u2984", u"\u2985", u"\u2986", u"\u2987", u"\u2988",
u"\u2989", u"\u298a", u"\u298b", u"\u298c", u"\u298d", u"\u298e", u"\u298f", u"\u2990",
u"\u2991", u"\u2992", u"\u2993", u"\u2994", u"\u2995", u"\u2996", u"\u2997", u"\u2998",
u"\u29d8", u"\u29d9", u"\u29da", u"\u29db", u"\u29fc", u"\u29fd", u"\u2cf9", u"\u2cfa",
u"\u2cfb", u"\u2cfc", u"\u2cfe", u"\u2cff", u"\u2e00", u"\u2e01", u"\u2e02", u"\u2e03",
u"\u2e04", u"\u2e05", u"\u2e06", u"\u2e07", u"\u2e08", u"\u2e09", u"\u2e0a", u"\u2e0b",
u"\u2e0c", u"\u2e0d", u"\u2e0e", u"\u2e0f", u"\u2e10", u"\u2e11", u"\u2e12", u"\u2e13",
u"\u2e14", u"\u2e15", u"\u2e16", u"\u2e17", u"\u2e18", u"\u2e19", u"\u2e1a", u"\u2e1b",
u"\u2e1c", u"\u2e1d", u"\u2e1e", u"\u2e1f", u"\u2e20", u"\u2e21", u"\u2e22", u"\u2e23",
u"\u2e24", u"\u2e25", u"\u2e26", u"\u2e27", u"\u2e28", u"\u2e29", u"\u2e2a", u"\u2e2b",
u"\u2e2c", u"\u2e2d", u"\u2e2e", u"\u2e30", u"\u2e31", u"\u3001", u"\u3002", u"\u3003",
u"\u3008", u"\u3009", u"\u300a", u"\u300b", u"\u300c", u"\u300d", u"\u300e", u"\u300f",
u"\u3010", u"\u3011", u"\u3014", u"\u3015", u"\u3016", u"\u3017", u"\u3018", u"\u3019",
u"\u301a", u"\u301b", u"\u301c", u"\u301d", u"\u301e", u"\u301f", u"\u3030", u"\u303d",
u"\u30a0", u"\u30fb", u"\ua4fe", u"\ua4ff", u"\ua60d", u"\ua60e", u"\ua60f", u"\ua673",
u"\ua67e", u"\ua6f2", u"\ua6f3", u"\ua6f4", u"\ua6f5", u"\ua6f6", u"\ua6f7", u"\ua874",
u"\ua875", u"\ua876", u"\ua877", u"\ua8ce", u"\ua8cf", u"\ua8f8", u"\ua8f9", u"\ua8fa",
u"\ua92e", u"\ua92f", u"\ua95f", u"\ua9c1", u"\ua9c2", u"\ua9c3", u"\ua9c4", u"\ua9c5",
u"\ua9c6", u"\ua9c7", u"\ua9c8", u"\ua9c9", u"\ua9ca", u"\ua9cb", u"\ua9cc", u"\ua9cd",
u"\ua9de", u"\ua9df", u"\uaa5c", u"\uaa5d", u"\uaa5e", u"\uaa5f", u"\uaade", u"\uaadf",
u"\uabeb", u"\ufd3e", u"\ufd3f", u"\ufe10", u"\ufe11", u"\ufe12", u"\ufe13", u"\ufe14",
u"\ufe15", u"\ufe16", u"\ufe17", u"\ufe18", u"\ufe19", u"\ufe30", u"\ufe31", u"\ufe32",
u"\ufe33", u"\ufe34", u"\ufe35", u"\ufe36", u"\ufe37", u"\ufe38", u"\ufe39", u"\ufe3a",
u"\ufe3b", u"\ufe3c", u"\ufe3d", u"\ufe3e", u"\ufe3f", u"\ufe40", u"\ufe41", u"\ufe42",
u"\ufe43", u"\ufe44", u"\ufe45", u"\ufe46", u"\ufe47", u"\ufe48", u"\ufe49", u"\ufe4a",
u"\ufe4b", u"\ufe4c", u"\ufe4d", u"\ufe4e", u"\ufe4f", u"\ufe50", u"\ufe51", u"\ufe52",
u"\ufe54", u"\ufe55", u"\ufe56", u"\ufe57", u"\ufe58", u"\ufe59", u"\ufe5a", u"\ufe5b",
u"\ufe5c", u"\ufe5d", u"\ufe5e", u"\ufe5f", u"\ufe60", u"\ufe61", u"\ufe63", u"\ufe68",
u"\ufe6a", u"\ufe6b", u"\uff01", u"\uff02", u"\uff03", u"\uff05", u"\uff06", u"\uff07",
u"\uff08", u"\uff09", u"\uff0a", u"\uff0c", u"\uff0d", u"\uff0e", u"\uff0f", u"\uff1a",
u"\uff1b", u"\uff1f", u"\uff20", u"\uff3b", u"\uff3c", u"\uff3d", u"\uff3f", u"\uff5b",
u"\uff5d", u"\uff5f", u"\uff60", u"\uff61", u"\uff62", u"\uff63", u"\uff64", u"\uff65"}

stopwords = {"a", "about", "an", "are", "as", "at", "be", "by", "com","for", "from", 
"how", "in", "is", "it", "of", "on", "or", "that", "the", "this","to", "was", 
"what", "when", "where", "who", "will", "with", "the", "www", "and","'s"}

wordD = dict()

def countwords(w):
  w = w.lower()
  if w in punct:
  	return
  if w in stopwords:
  	return
  if w in wordD:
  	wordD[w] += 1
  	return
  wordD[w] = 1

def countHeadlines(h):
	sent = h["Headline"]
	words = nltk.word_tokenize(sent)
	map(countwords,words)


for fname in os.listdir(dowjones):
	if fname.endswith('json'):
		jfile = codecs.open(dowjones+'/' + fname,'r','utf-8')
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
dictFile = codecs.open('dict_lowered.json','w','utf-8')
dictFile.write(json.dumps(sortedD))
dictFile.close()

dictTxt = codecs.open('dict_lowered.txt','w', 'utf-8')
for item in sortedD:
	dictTxt.write(u'%s\t%d\n' %(item[0],item[1]))
dictTxt.close()

