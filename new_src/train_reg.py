# author: Xiaote Zhu

import codecs
import json
import os
import datetime
import nltk
import creg_driver
import subprocess

XDir = "../new_result/trainData_reg+tempX"
YDir = "../new_result/trainData_regY_long"
weightDir = "../new_result/reg+temp_result"

for fname in os.listdir(XDir):
	print fname
	Xpath = '%s/%s' %(XDir,fname)
	stock = fname[:-5]
	Ypath = '%s/%s.txt' %(YDir,stock)
	weightPath = '%s/%s.txt' %(weightDir,stock)

	creg_driver.train((Xpath,Ypath),weights = weightPath, options = {'--l1': '1'})






