#!/bin/bash
# usb device driver autotest shell-script

set -e
#set -x

if [ $# -lt 3 ]; then
    echo "usage : $(basename $0) SOURCE_PATH DESTINATION_PATH FILE_SIZE"
    exit 1
fi

SRC_DIR="$1"
DST_DIR="$2"
FILE_SIZE="$3"

echo "read write ${FILE_SIZE}M file from $SRC_DIR to $DST_DIR"

# write test
echo "create data ${FILE_SIZE}mb on $SRC_DIR"
cmd="dd if=/dev/urandom of=${SRC_DIR}/file_${FILE_SIZE}mb bs=1M count=${FILE_SIZE}"
echo $cmd

eval $cmd

if ! [ -f ${SRC_DIR}/file_${FILE_SIZE}mb ];then
	echo "prepare data on $SRC_DIR not exits"
	eval $FAIL_MEG
	exit 1
fi

echo "copy data from $SRC_DIR to $DST_DIR"
cmd="cp ${SRC_DIR}/file_${FILE_SIZE}mb $DST_DIR"

echo $cmd

eval $cmd

sync

if ! cmp ${SRC_DIR}/file_${FILE_SIZE}mb ${DST_DIR}/file_${FILE_SIZE}mb;then
	echo "copy data from $SRC_DIR to $DST_DIR error"
	eval $FAIL_MEG
	exit 1
fi

#rm -rf ${SRC_DIR}/*
#rm -rf ${DST_DIR}/*

sync

sleep 3

#read test
echo "create ${FILE_SIZE}mb data on $DST_DIR"
cmd="dd if=/dev/urandom of=${DST_DIR}/file_${FILE_SIZE}mb bs=1M count=${FILE_SIZE}"
echo $cmd

eval $cmd

if ! [ -f ${DST_DIR}/file_${FILE_SIZE}mb ];then
	echo "prepare data on $DST_DIR not exits"
	eval $FAIL_MEG
	exit 1
fi

echo "copy data from $DST_DIR to $SRC_DIR"
cmd="cp ${DST_DIR}/file_${FILE_SIZE}mb $SRC_DIR"
echo $cmd

eval $cmd

sync

if ! cmp ${SRC_DIR}/file_${FILE_SIZE}mb ${DST_DIR}/file_${FILE_SIZE}mb;then
	echo "copy data from $DST_DIR to $SRC_DIR error"
	eval $FAIL_MEG
	exit 1
fi

eval $PASS_MEG

sync