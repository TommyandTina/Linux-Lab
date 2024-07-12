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
echo
echo "2.1.Normal System Test No.26"
echo

echo "insmod /lib/modules/`uname -r`/extra/memd.ko"
insmod /lib/modules/`uname -r`/extra/memd.ko

echo "echo rd 0xe61509a0 > /proc/reg"
sleep 1
echo rd 0xe61509a0 > /proc/reg

echo "Please check BIT15 = 0"
echo "Ex) 01F16FF5"

echo "rmmod memd"
rmmod memd

echo
echo "2.1.Normal System Test No.28"
echo
echo "cd /sys/bus/platform/drivers/sata_rcar; find -type l"
echo
cd /sys/bus/platform/drivers/sata_rcar; find -type l

echo
echo "echo ee300000.sata > unbind"
echo
echo ee300000.sata > unbind

echo
echo "ls -d ee300000.sata"
echo
ls -d ee300000.sata
if [ $? -eq 0 ]; then
	error_msg "unbind fail"
fi
	
echo
echo "ls /dev/sda"
echo
ls /dev/sda

echo
echo "echo ee300000.sata > bind"
echo
echo ee300000.sata > bind

echo
echo "ls -d ee300000.sata"
echo
ls -d ee300000.sata || error_msg "bind fail"

echo "----- Finish -----"
