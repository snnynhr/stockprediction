import json
import datetime
import nltk
import codecs
import random

trainDir = "../newData/trainRand"
testDir = "../newData/testRand"

dayStockPath= "../data/stocks/dayStock.json"
dayStockFile = codecs.open(dayStockPath,'r','utf-8')
dayStockDict = json.load(dayStockFile)

headlineDir = "../data/dowjones"

dictPath = '../data/dict/dict_lowered.json'
dictFile = codecs.open(dictPath, 'r','utf-8')
dictList = json.load(dictFile)
D = dict([(w[0], i) for i, w in enumerate(dictList)])

# 466 stocks in total
stockSet = set([u'AGN', u'EOG', u'WLP', u'CPB', u'YUM', u'JWN', u'TAP', u'AAPL',
u'SPG', u'FIS', u'GT', u'GIS', u'MJN', u'NWL', u'GE', u'GD', u'VAR', u'AMZN',
u'MAS', u'MAR', u'MAT', u'SNA', u'SNI', u'XRAY', u'JNJ', u'TSN', u'TSO', u'BEN',
u'CMI', u'EL', u'CMG', u'CME', u'DTE', u'PCL', u'CMS', u'DTV', u'VLO', u'HUM',
u'APOL', u'PCLN', u'FSLR', u'HCP', u'FTR', u'K', u'FFIV', u'BLL', u'CSC',
u'BLK', u'FTI', u'HCN', u'NFX', u'MA', u'CBG', u'PRGO', u'MO', u'NOC', u'MU',
u'CBS', u'NDAQ', u'SE', u'MS', u'TJX', u'NOV', u'AMGN', u'COST', u'FE', u'CTL',
u'ADBE', u'DOV', u'DOW', u'MSFT', u'GLW', u'SCHW', u'BSX', u'FCX', u'HSP',
u'BDX', u'WHR', u'BBBY', u'MDT', u'ZMH', u'F', u'DFS', u'JEC', u'V', u'FMC',
u'ALL', u'NTAP', u'LMT', u'MMM', u'SO', u'JNPR', u'MMC', u'CTSH', u'DPS',
u'IBM', u'BAX', u'CAT', u'CAH', u'BAC', u'CAM', u'GS', u'CAG', u'LO', u'LM',
u'TE', u'LH', u'PGR', u'HIG', u'CELG', u'A', u'ABC', u'ZION', u'STI', u'STJ',
u'STT', u'ABT', u'XOM', u'STX', u'STZ', u'BHI', u'CERN', u'RSG', u'PNW', u'AVB',
u'PNC', u'BXP', u'VFC', u'HAR', u'AON', u'RAI', u'PRU', u'RF', u'RL', u'URBN',
u'CHK', u'L', u'HRS', u'HRL', u'MRO', u'MRK', u'HRB', u'IPG', u'RHT', u'TYC',
u'RHI', u'APH', u'ROST', u'APC', u'APA', u'APD', u'KSS', u'WFM', u'WFC', u'IFF',
u'NVDA', u'LUK', u'RTN', u'BMS', u'BMY', u'AFL', u'DISCA', u'PAYX', u'OXY',
u'SHW', u'GCI', u'ED', u'EA', u'ORLY', u'CSX', u'EW', u'BTU', u'LUV', u'MUR',
u'ATI', u'WYN', u'JBL', u'ADSK', u'ECL', u'SNDK', u'SEE', u'DGX', u'NUE',
u'PCP', u'LNC', u'EXPD', u'UNP', u'ETFC', u'DUK', u'XL', u'CLF', u'R', u'CLX',
u'CMA', u'BBY', u'UNH', u'BBT', u'UNM', u'OMC', u'HP', u'KO', u'VMC', u'KR',
u'EXPE', u'KEY', u'ITW', u'KLAC', u'DO', u'SWK', u'PNR', u'WYNN', u'SWN', u'DF',
u'DD', u'DE', u'SWY', u'TGT', u'HBAN', u'BIG', u'BIIB', u'PCG', u'POM', u'AKAM',
u'DHI', u'M', u'INTU', u'SLM', u'ALXN', u'DHR', u'SLB', u'MCO', u'MCK', u'MCD',
u'NRG', u'PBCT', u'VTR', u'AXP', u'NFLX', u'EXC', u'WM', u'DNR', u'SRCL', u'WU',
u'WY', u'VNO', u'SPLS', u'HST', u'HSY', u'WEC', u'HAL', u'FITB', u'EQR', u'EQT',
u'GPC', u'X', u'XLNX', u'HAS', u'THC', u'PH', u'GPS', u'PHM', u'SYK', u'BRCM',
u'SYY', u'AEP', u'AES', u'AET', u'EMC', u'EMN', u'GRMN', u'ESRX', u'AMAT',
u'IGT', u'AEE', u'CTAS', u'EMR', u'FDX', u'CRM', u'NWSA', u'PX', u'PG', u'CTXS',
u'PM', u'EFX', u'C', u'S', u'QCOM', u'XRX', u'ANF', u'MOS', u'PSA', u'MON',
u'JOY', u'MCHP', u'ALTR', u'ETR', u'COP', u'DVN', u'KMB', u'COV', u'DVA',
u'GWW', u'FISV', u'COG', u'COF', u'COH', u'TMK', u'ETN', u'COL', u'BCR', u'KMX',
u'FDO', u'DLTR', u'CI', u'JDSU', u'SRE', u'WAG', u'CB', u'CA', u'CF', u'WAT',
u'CHRW', u'TDC', u'SBUX', u'PLD', u'HCBK', u'PLL', u'CL', u'CMCSA', u'FHN',
u'MKC', u'GNW', u'CVX', u'AIZ', u'EIX', u'AIV', u'CVS', u'LOW', u'MSI', u'AIG',
u'CVC', u'DIS', u'PPG', u'MNST', u'NSC', u'GAS', u'PPL', u'OKE', u'GOOG',
u'JCP', u'IP', u'HPQ', u'IR', u'IRM', u'MTB', u'UTX', u'JCI', u'PWR', u'CSCO',
u'ARG', u'WDC', u'BA', u'BK', u'DRI', u'CCL', u'CCI', u'CCE', u'TIF', u'FLIR',
u'SYMC', u'MYL', u'SIAL', u'D', u'PEP', u'WMT', u'VZ', u'T', u'WMB', u'VRSN',
u'OI', u'CINF', u'NTRS', u'MWV', u'HOG', u'FLS', u'FLR', u'HD', u'LLY', u'PEG',
u'INTC', u'SCG', u'AMD', u'LLL', u'ROP', u'AMP', u'TMO', u'AMT', u'LRCX',
u'ICE', u'YHOO', u'PBI', u'UPS', u'TRV', u'AVY', u'AVP', u'MDLZ', u'IVZ',
u'NEM', u'FOSL', u'ACE', u'NEE', u'ACN', u'NI', u'TEL', u'NBR', u'RRC', u'NE',
u'FAST', u'TEG', u'NBL', u'TER', u'NU', u'LLTC', u'ADP', u'DNB', u'GILD',
u'GME', u'RDC', u'SJM', u'JPM', u'ADM', u'ADI', u'VIAB', u'LEG', u'XEL', u'WIN',
u'LEN', u'EBAY', u'MET', u'TWC', u'USB', u'AZO', u'PDCO', u'TWX', u'PCAR',
u'TXN', u'PETM', u'HES', u'ORCL', u'TXT', u'PXD', u'AA', u'ESV', u'PKI', u'CNP',
u'HON', u'CNX', u'AN', u'HOT', u'ROK', u'TROW', u'ISRG', u'PFE', u'NKE', u'PFG',
u'TSS'])

testDays = []
trainDays = []
allDays = dayStockDict.keys()
total = len(allDays)
random.shuffle(allDays)
#for day in dayStockDict:
#	if int(day[:6]) >= 201204:
#		testDays.append(day)
#	else:
#		trainDays.append(day)

i = int(total * 0.7)
trainDays = allDays[:i]
testDays = allDays[i:]
testDays.sort()
trainDays.sort()
allDays.sort()
print total

# for sparse ones: allD is a dictionary of dictionary
# headlines are all before 9:30 EST
def featureAMs(allD,headlineD, stock):
	headlines = headlineD["Headlines"]
	for h in headlines:
		sent = h["Headline"]
		words = nltk.word_tokenize(sent)
		c_time_str = h["CreateTimestamp"]["Value"]
		c_time = datetime.datetime.strptime(c_time_str, "%Y-%m-%dT%H:%M:%S")
		if c_time.hour >= 14 and c_time.minute >= 30:
			c_date_str = (c_time + datetime.timedelta(days=1)).strftime("%Y%m%d")
		else:
			c_date_str = c_time.strftime("%Y%m%d")
		if int(c_date_str) < int(trainDays[0]):
			continue
		if c_date_str not in allD:
			allD[c_date_str] = dict()
		if stock not in allD[c_date_str]:
			allD[c_date_str][stock] = dict()
		for w in words:
			if w in D:
				key = "%s_%s" %(stock,w)
				if key in allD[c_date_str][stock]:
					allD[c_date_str][stock][key] += 1
				else:
					allD[c_date_str][stock][key] = 1

def writeToFile(dayList,filePath,prevDayP = None):
	stockD = dict()
	for day in dayList:

		if stock not in dayStockDict[day]:
			continue

		dayP = dayStockDict[day][stock]
		if prevDayP == None:
			prevDayP = dayP
			continue

		if dayP > prevDayP:
			change = "r_up"
		else:
			change = "r_down"

		stockD[day] = dict()
		stockD[day]["change"] = change
		stockD[day]["cur_price"] = dayP
		stockD[day]["prev_price"] = prevDayP

		if day in allD:
			stockD[day]["features"] = allD[day]
		prevDayP = dayP

	output_file = codecs.open(filePath,'w','utf-8') 
	output_file.write(json.dumps(stockD,indent=2))
	output_file.close()
	return prevDayP

def writeBoth(stock,trainDays,testDays,allDays,trainPath,testPath,prevDayP = None):
	trainD = dict()
	testD = dict()
	for i in xrange(0,total):
		day = allDays[i]

		if stock not in dayStockDict[day]:
			continue

		dayP = dayStockDict[day][stock]
		if prevDayP == None:
			prevDayP = dayP
			continue

		if dayP > prevDayP:
			change = "r_up"
		else:
			change = "r_down"

		if day in trainDays:
			trainD[day] = dict()
			trainD[day]["change"] = change
			trainD[day]["cur_price"] = dayP
			trainD[day]["prev_price"] = prevDayP
			if day in allD:
				trainD[day]["features"] = allD[day]
		else:
			testD[day] = dict()
			testD[day]["change"] = change
			testD[day]["cur_price"] = dayP
			testD[day]["prev_price"] = prevDayP
			if day in allD:
				testD[day]["features"] = allD[day]

		prevDayP = dayP

	train_file = codecs.open(trainPath,'w','utf-8') 
	train_file.write(json.dumps(trainD,indent=2))
	train_file.close()

	test_file = codecs.open(testPath,'w','utf-8') 
	test_file.write(json.dumps(testD,indent=2))
	test_file.close()

allD = dict()
for stock in stockSet:
	print "extracting headlines related to %s..." %stock
	headlineFile = codecs.open('%s/%s.json' %(headlineDir,stock),'r','utf-8')
	headlineD = json.load(headlineFile)

	featureAMs(allD,headlineD,stock)

	headlineFile.close()


for stock in stockSet:
	print "writing for %s..." %stock
	trainPath = "%s/%s.json" %(trainDir,stock)
	testPath = "%s/%s.json" %(testDir,stock)
	writeBoth(stock,trainDays,testDays,allDays,trainPath,testPath,prevDayP = None)

	# trainPath = "%s/%s.json" %(trainDir,stock)
	# prevDayP = writeToFile(trainDays,trainPath,None)
	# testPath = "%s/%s.json" %(testDir,stock)
	# prevDayP = writeToFile(testDays,testPath,prevDayP)
