#!/bin/bash

usage()
{
cat << EOF
	usage: `basename $0` [-xs] <target>
	-xs: Salvator-XS
	target: HDD or DVD

	Ex)
	`basename $0` -xs HDD
EOF
}

##### include #####
. `dirname $0`/sata_common.func

##### argument #####
if [ $# == 0 ]; then
	usage
	exit 1
fi

TARGET=""
_salvator_xs=0
while [ $# -gt 0 ]; do
	case "$1" in
		-xs)
			_salvator_xs=1
			;;
		HDD | DVD)
			TARGET=$1
			;;
		*)
			usage
			exit 1
			;;
	esac
	shift
done

echo "TARGET=$TARGET"
echo "_salvator_xs=$_salvator_xs"

if [ "X$TARGET" == "X" ] ; then
	echo "Select HDD or DVD"
	exit 1
fi

##### For Salvator-XS #####
if [ ${_salvator_xs} -eq 1 ]; then
	echo "Initialize for Salvator-XS"
	sata_start_i2c
	sata_module_install "INSMOD"
fi

##### main #####
echo
echo "2.2.Abnormal System Test"
echo

if [ $TARGET == "HDD" ] ; then
	echo "2.2 Abnormal System Test No.1"
	echo
	echo "dd if=/dev/zero of=/dev/sda bs=512 count=1 seek=999999999"
	echo
	dd if=/dev/zero of=/dev/sda bs=512 count=1 seek=999999999

	echo
	echo "2.2 Abnormal System Test No.2"
	echo
	echo "dd if=/dev/sda of=/dev/null bs=512 count=1 skip=999999999"
	echo
	dd if=/dev/sda of=/dev/null bs=512 count=1 skip=999999999

	echo "2.2 Abnormal System Test No.5"
	echo
	echo "Please disconnect SATA cable, during dd command"
	echo "After 5s, dd command will be executed"
	echo "sleep 5"
	sleep 5
	echo "dd if=/dev/zero of=/dev/sda1 bs=1M count=1000"
	dd if=/dev/zero of=/dev/sda1 bs=1M count=1000
	echo "dd end"

elif [ $TARGET == "DVD" ] ; then
	echo
	echo "2.2 Abnormal System Test No.3"
	echo
	echo "dd if=/dev/sr0 of=/dev/null bs=2048 count=102400 &"
	echo
	dd if=/dev/sr0 of=/dev/null bs=2048 count=102400 &
	pid=$!
	echo
	echo "eject"
	echo
	eject
	echo
	echo "eject -t"
	echo
	eject -t
	echo
	echo "Wait for finish dd cmd ($pid)"
	wait $pid

	echo "Wait for Media Ready"
	echo "sleep 20"
	sleep 20
 
	echo "2.2 Abnormal System Test No.4"
	echo
	echo "dd if=/dev/sr0 of=aaa bs=2048 count=1 skip=999999"
	echo
	dd if=/dev/sr0 of=aaa bs=2048 count=1 skip=999999
	echo
	echo "ls -l aaa"
	ls -l aaa
	echo
fi

echo "----- Finish -----"
