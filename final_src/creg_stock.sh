#!/bin/sh

module load creg-2014-02-18 
WORKING_DIR="/home/ysim/xiaote/stockprediction"
STOCK="${1}"
creg -x ${WORKING_DIR}/newData/trainXRandAll/${STOCK}.json -y ${WORKING_DIR}/newData/trainYRandAll/${STOCK}.txt --l1 1 --z ${WORKING_DIR}/newData/weightRandAll/${STOCK}.txt 2> /dev/null
echo ${STOCK} done

# parallel --verbose --jobs 12 --progress --bar ./creg_stock.sh :::: stock_list.txt

