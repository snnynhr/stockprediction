# author: Xiaote Zhu

def discrete(d):
	prev = None
	L = []
	for date in sorted(d):
		if prev != None:
			cur = d[date]
			if cur < prev:
				L.append((date,-1))
			else:
				L.append((date, 1))
			prev = cur
		else:
			prev = d[date]
	return L
