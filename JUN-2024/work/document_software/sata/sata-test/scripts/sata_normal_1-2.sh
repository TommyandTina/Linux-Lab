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
echo "2.1.Normal System Test No.1"
echo

echo "dmesg | grep ata1"
dmesg | grep ata1

echo
echo "expect No1 ex)"
echo "ata1: SATA max UDMA/133 irq 31"
echo "ata1: link resume succeeded after 1 retries"
echo "ata1: SATA link down (SStatus 0 SControl 300)"

echo
echo "2.1.Normal System Test No.2"
echo

echo "cat /proc/interrupts | grep sata"
cat /proc/interrupts | grep sata

echo
echo "expect No2 ex)"
echo " 31:          0          0          0          0       GIC 137 Level     ee300000.sata"

echo "---- Finish -----"
