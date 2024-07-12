#!/bin/bash

usage()
{
cat << EOF
	usage: `basename $0` [-i] [-o <output dir>][-best] [qos file]
	device file: /dev/mmcblk1p1
	qos file: QoS CVS file (*.csv)
	-i: IPMMU OFF
	-o: Output file directory (default is ./cpuload)
	-best: Best performance QoS test.

	Ex)
	`basename $0` -o /home/result
EOF
}

##### argument #####
if [ $# == 0 ]; then
	usage
	exit 1
fi

OUT_DIR=./cpuload
START_NUM=2
QOS_OFFSET=0
_small=1
_large=1
_e3=0
_d3=0
_v3x=0
_v3u=0
_format=0
_qos=0
_ipmmu=0
while [ $# -gt 0 ]; do
	case "$1" in
		*.csv)
			QOS_FILE=$1
			_qos=1
			QOS_OFFSET=2
			;;
		-i)
			_ipmmu=0
			;;
		-o)
			shift
			OUT_DIR=$1
			;;
		-best)
			;;
		-e3 | -v3x | -v3h | -v3m | -v3u)
			;;
		-f)
			_format=1
			;;
		*)
			usage
			exit 1
			;;
	esac
	shift
done

##### Main #####
BS=1M
COUNT=1024

DEVFILE=/dev/sda

# sanity check
if [ ! -e $DEVFILE ]; then
	error_msg "Not found $DEVFILE"
	usage
	exit 1
fi

echo "mkdir -p $OUT_DIR"
mkdir -p $OUT_DIR

# QoS Setting
if [ $_qos == 1 ]; then
        echo "modprobe qos"
        modprobe qos || error_msg "modprobe fail"
        echo "qos_tp setall $QOS_FILE"
        qos_tp setall $QOS_FILE || error_msg "qos_tp fail"
        echo "qos_tp switch"
        qos_tp switch || error_msg "qos_tp fail"
fi

TESTNUM=`expr $START_NUM + $QOS_OFFSET`

echo
echo "3.1.Performance  test No.${TESTNUM}"
echo

if [ -e $OUT_DIR/3.1.$TESTNUM.r.txt ]; then
	echo "$OUT_DIR/3.1.$TESTNUM.r.txt exist"
	echo "Hit any key (Over write) or CTRL+C"
	read
fi

echo "time dd if=$DEVFILE of=/dev/null bs=$BS count=$COUNT iflag=direct & top -b -d 1 -n 10 > $OUT_DIR/3.1.$TESTNUM.r.txt"
time dd if=$DEVFILE of=/dev/null bs=$BS count=$COUNT iflag=direct & top -b -d 1 -n 10 > $OUT_DIR/3.1.$TESTNUM.r.txt
pid=$!
echo "wait PID=$pid"
wait $pid
echo "wait done"
sleep 1

if [ -e $OUT_DIR/3.1.$TESTNUM.w.txt ]; then
	echo "$OUT_DIR/3.1.$TESTNUM.w.txt exist"
	echo "Hit any key (Over write) or CTRL+C"
	read
fi

echo "time dd if=/dev/zero of=$DEVFILE bs=$BS count=$COUNT oflag=direct & top -b -d 1 -n 10 > $OUT_DIR/3.1.$TESTNUM.w.txt"
time dd if=/dev/zero of=$DEVFILE bs=$BS count=$COUNT oflag=direct & top -b -d 1 -n 10 > $OUT_DIR/3.1.$TESTNUM.w.txt

pid=$!
echo "wait PID=$pid"
wait $pid
echo "wait done"
sleep 1

echo "----- Finish -----"
