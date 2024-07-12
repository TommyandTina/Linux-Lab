#!/bin/bash

usage()
{
cat << EOF
	usage: `basename $0` [-xs]
	-xs: Salvator-XS

	Ex)
	`basename $0` -xs
EOF
}

##### include #####
. `dirname $0`/sata_common.func

##### argument #####
if [ $# -gt 1 ]; then
	usage
	exit 1
fi

_salvator_xs=0
while [ $# -gt 0 ]; do
	case "$1" in
		-xs)
			_salvator_xs=1
			;;
		*)
			usage
			exit 1
			;;
	esac
	shift
done

##### For Salvator-XS #####
if [ ${_salvator_xs} -eq 1 ]; then
	echo "Initialize for Salvator-XS"
	sata_start_i2c
	sata_module_install "INSMOD"
fi

##### main #####
ORG_FILE=/tmp/test_org.dat
COPY_FILE_A=/tmp/test_a.dat
COPY_FILE_B=/tmp/test_b.dat
TEST_TIME=0
START_TIME=`date +%s`
END_TIME=1800

echo "END_TIME=$END_TIME"

echo "3.3 Durability Load Test No.1"
echo

echo "mkdir -p /mnt/sata"
mkdir -p /mnt/sata || error_msg "mkdir fail"
echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata || error_msg "mount fail"

echo "dd if=/dev/urandom of=$ORG_FILE bs=1M count=1"
dd if=/dev/urandom of=$ORG_FILE bs=1M count=1 || error_msg "create $ORG_FILE fail"

echo "cp $ORG_FILE $COPY_FILE_A"
cp $ORG_FILE $COPY_FILE_A || error_msg "cp fail"

until [ `expr $TEST_TIME / $END_TIME` -ge 1 ];
do
	echo "$TEST_TIME"
	echo "dd if=$COPY_FILE_A of=/mnt/sata/tmp.dat bs=1M count=1"
	dd if=$COPY_FILE_A of=/mnt/sata/tmp.dat bs=1M count=1 || error_msg "dd fail"
	sleep 1
	echo "dd if=/mnt/sata/tmp.dat of=$COPY_FILE_B bs=1M count=1"
	dd if=/mnt/sata/tmp.dat of=$COPY_FILE_B bs=1M count=1 || error_msg "dd fail"
	echo "mv $COPY_FILE_B $COPY_FILE_A"
	mv $COPY_FILE_B $COPY_FILE_A

	GET_TIME=`date +%s`
	TEST_TIME=`expr $GET_TIME - $START_TIME`
done

echo "cmp $COPY_FILE_A $ORG_FILE"
cmp $COPY_FILE_A $ORG_FILE || error_msg "compare fail"

echo "rm $ORG_FILE $COPY_FILE_A /mnt/sata/tmp.dat"
rm $ORG_FILE $COPY_FILE_A /mnt/sata/tmp.dat || error_msg "rm fail"

echo "sync"
sync
echo "umount /mnt/sata"
umount /mnt/sata || error_msg "umount fail"
echo "rmdir /mnt/sata"
rmdir /mnt/sata || error_msg "rmdir fail"

echo "----- Finish -----"
