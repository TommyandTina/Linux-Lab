#!/bin/bash

usage()
{
cat << EOF
usage: `basename $0` [-xs] <Number of Process>
	-xs: Salvator-XS
	Number of Process: Create Process number

	Ex)
	`basename $0` -xs 4
EOF
}

##### include #####
. `dirname $0`/sata_common.func

##### argument #####
if [ $# == 0 ]; then
	usage
	exit 1
fi

_salvator_xs=0
_pnum=0
while [ $# -gt 0 ]; do
	case "$1" in
		-xs)
			_salvator_xs=1
			;;
		[1-9]*)
			_pnum=$1
			;;
		*)
			usage
			exit 1
			;;
	esac
	shift
done

if [ _pnum == 0 ]; then
	usage
	exit 1
fi

##### For Salvator-XS #####
if [ ${_salvator_xs} -eq 1 ]; then
	echo "Initialize for Salvator-XS"
	sata_start_i2c
	sata_module_install "INSMOD"
fi

echo
echo "3.2 SMP Multi-Instance Test No.1"

for ((i=1; i<_pnum; i++))
do
	echo "taskset -c $i ./sata_pfm_onece.sh &"
	taskset -c $i ./sata_pfm_onece.sh &
done

echo "taskset -c $i ./sata_pfm_onece.sh"
taskset -c $i ./sata_pfm_onece.sh

echo "----- Finish -----"
