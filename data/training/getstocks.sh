#!/bin/bash
# prices from S&P500 can be downloaded from
#http://www2.standardandpoors.com/portal/site/sp/en/us/page.topic/indices_500/2,3,2,2,0,0,0,0,0,2,3,0,0,0,0,0.html

# We download from today to the date in the command line

#./yahooDown.sh standardPoorList.csv DestDir 1-1-1995
# e.g. ./yahooDown.sh 17-FEB-2009_1000.csv SP1000 1-1-1995

todayDate=$(date "+%d %m %Y")

# Start date
sDay=$(echo $todayDate | awk '{print $1}')
sMonth=$(echo $todayDate | awk '{print $2}')
sYear=$(echo $todayDate | awk '{print $3}')

# end date

eDay=$(echo $3 | sed "s:-: :g" | awk '{print $1}')
eMonth=$(echo $3 |sed "s:-: :g" | awk '{print $2}')
eYear=$(echo $3 |sed "s:-: :g" | awk '{print $3}')

# command to fetch data the CSV files from yahoo

DESTDIR=$2
WGET="curl"
OPT1="-o"

COM1="http://ichart.finance.yahoo.com/table.csv?s="
COMd="&d="$(expr $sMonth - 1)
COMe="&e="
COMf="&f="
COMg="&g=d"
COMa="&a="$(expr $eMonth - 1)
COMb="&b="
COMc="&c="
COMlast="&ignore=.csv"

# the command we pass to wget
for i in $(sed -e "s:,: :" -e "/Symbol*/ d" -e "/^$/ d" $1 | awk '{print $1}'); do

echo "Downloading the data for symbol " $i
WEBURL="$COM1$i$COMa$COMb$eMonth$COMc$eYear$COMd$COMe$sMonth$COMf$sYear$COMg$COMlast"
COMMAND="$WGET $OPT1"$DESTDIR/$i.csv" "$WEBURL""
$COMMAND

done