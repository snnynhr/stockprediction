there are 484 stocks
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 PKI &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 HRS &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 T &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 CNP &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 TYC &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 GCI &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 DIS &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 LLL &
wait
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 CPB &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 PCLN &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 PHM &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 TMK &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 MSFT &
python regMainBs.py 1 ../XYdata/5 ../XYdata/5/weight1 ../XYdata/5/result1 DOW &
pytho[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:[29;63H8,1[11CTop[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:[29;67H8,1[11CTop[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, ree[30;1H[38;5;130m    [msultdir, stock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'[34;67H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resull[30;1H[38;5;130m    [mtdir, stock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'[34;70H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resull[30;1H[38;5;130m    [mtdir, stock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                      [35;1H~                                                                                      [36;1H~                                                                                      [37;1H~                                                                                      [38;1H~                                                                                      [m[39;70H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdii[30;1H[38;5;130m    [mr, stock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                         [35;1H~                                                                                         [36;1H~                                                                                         [37;1H~                                                                                         [38;1H~                                                                                         [m[39;73H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdii[30;1H[38;5;130m    [mr, stock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                         [35;1H~                                                                                         [36;1H~                                                                                         [37;1H~                                                                                         [38;1H~                                                                                         [39;1H~                                                                                         [40;1H~                                                                                         [41;1H~                                                                                         [42;1H~                                                                                         [m[43;73H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir,  [30;1H[38;5;130m    [mstock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                            [35;1H~                                                                                            [36;1H~                                                                                            [37;1H~                                                                                            [38;1H~                                                                                            [39;1H~                                                                                            [40;1H~                                                                                            [41;1H~                                                                                            [42;1H~                                                                                            [m[43;76H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir,  [30;1H[38;5;130m    [mstock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                            [35;1H~                                                                                            [36;1H~                                                                                            [37;1H~                                                                                            [38;1H~                                                                                            [39;1H~                                                                                            [40;1H~                                                                                            [41;1H~                                                                                            [42;1H~                                                                                            [43;1H~                                                                                            [44;1H~                                                                                            [45;1H~                                                                                            [m[46;76H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir, stt[30;1H[38;5;130m    [mock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                              [35;1H~                                                                                              [36;1H~                                                                                              [37;1H~                                                                                              [38;1H~                                                                                              [39;1H~                                                                                              [40;1H~                                                                                              [41;1H~                                                                                              [42;1H~                                                                                              [43;1H~                                                                                              [44;1H~                                                                                              [45;1H~                                                                                              [m[46;78H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir, stt[30;1H[38;5;130m    [mock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                              [35;1H~                                                                                              [36;1H~                                                                                              [37;1H~                                                                                              [38;1H~                                                                                              [39;1H~                                                                                              [40;1H~                                                                                              [41;1H~                                                                                              [42;1H~                                                                                              [43;1H~                                                                                              [44;1H~                                                                                              [45;1H~                                                                                              [46;1H~                                                                                              [m[47;78H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir, stocc[30;1H[38;5;130m    [mk)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                                [35;1H~                                                                                                [36;1H~                                                                                                [37;1H~                                                                                                [38;1H~                                                                                                [39;1H~                                                                                                [40;1H~                                                                                                [41;1H~                                                                                                [42;1H~                                                                                                [43;1H~                                                                                                [44;1H~                                                                                                [45;1H~                                                                                                [46;1H~                                                                                                [m[47;80H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir, stockk[30;1H[38;5;130m    [m)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                                 [35;1H~                                                                                                 [36;1H~                                                                                                 [37;1H~                                                                                                 [38;1H~                                                                                                 [39;1H~                                                                                                 [40;1H~                                                                                                 [41;1H~                                                                                                 [42;1H~                                                                                                 [43;1H~                                                                                                 [44;1H~                                                                                                 [45;1H~                                                                                                 [46;1H~                                                                                                 [m[47;81H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir, stock)[30;1H[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                                  [34;1H~                                                                                                  [35;1H~                                                                                                  [36;1H~                                                                                                  [37;1H~                                                                                                  [38;1H~                                                                                                  [39;1H~                                                                                                  [40;1H~                                                                                                  [41;1H~                                                                                                  [42;1H~                                                                                                  [43;1H~                                                                                                  [44;1H~                                                                                                  [45;1H~                                                                                                  [46;1H~                                                                                                  [m[47;82H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir, stock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                                     [34;1H~                                                                                                     [35;1H~                                                                                                     [36;1H~                                                                                                     [37;1H~                                                                                                     [38;1H~                                                                                                     [39;1H~                                                                                                     [40;1H~                                                                                                     [41;1H~                                                                                                     [42;1H~                                                                                                     [43;1H~                                                                                                     [44;1H~                                                                                                     [45;1H~                                                                                                     [46;1H~                                                                                                     [m[47;85H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir, stock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                                        [34;1H~                                                                                                        [35;1H~                                                                                                        [36;1H~                                                                                                        [37;1H~                                                                                                        [38;1H~                                                                                                        [39;1H~                                                                                                        [40;1H~                                                                                                        [41;1H~                                                                                                        [42;1H~                                                                                                        [43;1H~                                                                                                        [44;1H~                                                                                                        [45;1H~                                                                                                        [46;1H~                                                                                                        [m[47;88H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir, stock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                                           [34;1H~                                                                                                           [35;1H~                                                                                                           [36;1H~                                                                                                           [37;1H~                                                                                                           [38;1H~                                                                                                           [39;1H~                                                                                                           [40;1H~                                                                                                           [41;1H~                                                                                                           [42;1H~                                                                                                           [43;1H~                                                                                                           [44;1H~                                                                                                           [45;1H~                                                                                                           [46;1H~                                                                                                           [m[47;91H8,1[11CAll[8;5H[?12l[?25h[27m[m[H[2J[?25l[1;1H[38;5;130m  1 [m[35mimport[m os
[38;5;130m  2 [m[35mimport[m random
[38;5;130m  3 [m[35mimport[m json
[38;5;130m  4 [m[35mimport[m creg_driver
[38;5;130m  5 [m[35mimport[m operator
[38;5;130m  6 [m[35mimport[m sys
[38;5;130m  7 
  8 [mdatadir = '[31m../XYdata/5[m'
[38;5;130m  9 
 10 [mstockfile = open(datadir + '[31m/[m' + '[31mstock.txt[m', '[31mr[m')
[38;5;130m 11 [mstockList = stockfile.readline().strip().split('[35m\t[m')
[38;5;130m 12 print[m "[31mthere are[m", len(stockList), "[31mstocks[m"
[38;5;130m 13 [mstockfile.close()
[38;5;130m 14 
 15 [ml1 = sys.argv[1]
[38;5;130m 16 
 17 [mweightdir = '[31m%s/weight%s[m' % (datadir, l1)
[38;5;130m 18 if[m [38;5;130mnot[m os.path.exists(weightdir):
[38;5;130m 19 [m    os.makedirs(weightdir)
[38;5;130m 20 
 21 [mresultdir = '[31m%s/result%s[m' % (datadir, l1)
[38;5;130m 22 if[m [38;5;130mnot[m os.path.exists(resultdir):
[38;5;130m 23 [m    os.makedirs(resultdir)
[38;5;130m 24 
 25 [mpythonFile = '[31mregMainBs.py[m'
[38;5;130m 26 
 27 [mcount = 0
[38;5;130m 28 for[m stock [38;5;130min[m stockList:
[38;5;130m 29 [m    [38;5;130mprint[m '[31mpython %s %s %s %s %s %s &[m' % (pythonFile, l1, datadir, weightdir, resultdir, stock)
[38;5;130m 30 [m    count += 1
[38;5;130m 31 [m    [38;5;130mif[m count % 8 == 0:
[38;5;130m 32 [m[7C [38;5;130mprint[m '[31mwait[m'
[94m~                                                                                                                                                                                                                                             [34;1H~                                                                                                                                                                                                                                             [35;1H~                                                                                                                                                                                                                                             [36;1H~                                                                                                                                                                                                                                             [37;1H~                                                                                                                                                                                                                                             [38;1H~                                                                                                                                                                                                                                             [39;1H~                                                                                                                                                                                                                                             [40;1H~                                                                                                                                                                                                                                             [41;1H~                                                                                                                                                                                                                                             [42;1H~                                                                                                                                                                                                                                             [43;1H~                                                                                                                                                                                                                                             [44;1H~                                                                                                                                                                                                                                             [45;1H~                                                                                                                                                                                                                                             [46;1H~                                                                                                                                                                                                                                             [47;1H~                                                                                                                                                                                                                                             [48;1H~                                                                                                                                                                                                                                             [49;1H~                                                                                                                                                                                                                                             [50;1H~                                                                                                                                                                                                                                             [51;1H~                                                                                                                                                                                                                                             [52;1H~                                                                                                                                                                                                                                             [53;1H~                                                                                                                                                                                                                                             [54;1H~                                                                                                                                                                                                                                             [55;1H~                                                                                                                                                                                                                                             [56;1H~                                                                                                                                                                                                                                             [57;1H~                                                                                                                                                                                                                                             [58;1H~                                                                                                                                                                                                                                             [59;1H~                                                                                                                                                                                                                                             [60;1H~                                                                                                                                                                                                                                             [61;1H~                                                                                                                                                                                                                                             [62;1H~                                                                                                                                                                                                                                             [m[63;221H8,1[11CAll[8;5H[?12l[?25h