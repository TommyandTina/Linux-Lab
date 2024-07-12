#!/bin/sh
# ethernet device driver autotest shell-script

set -e
#set -x

LOGFILE="ether_log.txt"
PCNAME="rvc"
PCPASSWORD="Pass1234"
PC_FOLDER="/home/rvc/test_ether"
PASS_MEG="echo TEST_OK"
FAIL_MEG="echo TEST_NG"

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

RANDOM=`tr -cd 0-9 </dev/urandom | head -c 10`

LOGFILE="${RANDOM}-${LOGFILE}"

echo "prepare data for test"

#check file on host pc
ftp -inv $IPSERVER > $LOGFILE 2>&1 <<END_SCRIPT

quote USER $PCNAME
quote PASS $PCPASSWORD

ls $PC_FOLDER

quit

END_SCRIPT
#---------

if grep -i "file-${SIZE_DATA}mb" $LOGFILE >/dev/null;then
	echo "prepare data file-${SIZE_DATA}mb successfully"
else
	echo "prepare data file-${SIZE_DATA}mb not successfully please create data on host pc"
	rm -rf $LOGFILE
	eval $FAIL_MEG
	exit 1;	
fi

if [ -f $LOGFILE ];then
    rm -rf $LOGFILE
fi 

echo "tranfer file ${SIZE_DATA}MB"
$(dirname $0)/ftp_get_pc_to_board_data.sh $SIZE_DATA

sync
