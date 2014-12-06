import codecs
import os

inputDir = "../new_result/trainData_sage"
outputFile = "../new_result/train.txt"
out = codecs.open(outputFile, 'w', 'utf-8')
for Xfname in os.listdir(inputDir):
	if Xfname.endswith('.txt'):
		Xfile = codecs.open('%s/%s' % (inputDir, Xfname), 'r', 'utf-8')
		out.write(Xfile.read())
