#!/bin/sh
# ethernet device driver autotest shell-script

set -a
#set -x

LOGFILE="ether_log.txt"
LOGFILE="${RANDOM}-${LOGFILE}"
PASS_MEG="echo TEST_OK"
FAIL_MEG="echo TEST_NG"
PCNAME="rvc"
PCPASSWORD="Pass1234"
RAM_DIR="/tmp"
PC_FOLDER="/home/rvc/test_ether"

if [ $# -gt 1 ]; then
    echo "usage: $(basename $0) SIZE_DATA(MB)" >& 2
    echo "example: $(basename $0) 100"
    echo "default: 300MB"
    exit 1
fi

if [ $# -eq 1 ]; then
	SIZE_DATA="$1"
else
	SIZE_DATA=300
fi

echo "login server PC and tranfer data file"

ftp -inv $IPSERVER > $LOGFILE 2>&1 <<END_SCRIPT

	quote USER $PCNAME
	quote PASS $PCPASSWORD

	get $PC_FOLDER/file-${SIZE_DATA}mb ${RAM_DIR}/file-${SIZE_DATA}mb 

	quit

END_SCRIPT

echo "end tranfer data file"

if cat $LOGFILE | grep -i "Transfer complete" > /dev/null;then
	eval $PASS_MEG
else
	cat $LOGFILE
	eval $FAIL_MEG
fi 

if [ -f $LOGFILE ];then
    rm -rf $LOGFILE
fi
