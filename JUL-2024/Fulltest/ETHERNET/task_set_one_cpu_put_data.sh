#!/bin/sh
# ethernet device driver autotest shell-script

set -e
#set -x

LOGFILE="ether_log.txt"
RAM_DIR="/tmp"

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

echo "prepare data for test file-${SIZE_DATA}mb"

if ! [ -f "$(dirname $0)/data/file-${SIZE_DATA}mb" ]; then
	dd if=/dev/urandom of=${RAM_DIR}/file-${SIZE_DATA}mb bs=1M count=${SIZE_DATA}
else
	cp $(dirname $0)/data/file-${SIZE_DATA}mb $RAM_DIR/
	sync
fi

if [ -f "${RAM_DIR}/file-${SIZE_DATA}mb" ];then
	echo "prepare data file-${SIZE_DATA}mb successfully"
else
	echo "prepare data file-${SIZE_DATA}mb not successfully"
	eval $FAIL_MEG
	exit 1;	
fi

echo "tranfer file ${SIZE_DATA}MB"
$(dirname $0)/ftp_put_board_to_pc_data.sh $SIZE_DATA

sync