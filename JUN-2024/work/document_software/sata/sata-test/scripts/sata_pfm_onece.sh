#!/bin/bash
#
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
echo "dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=100 skip=1000"
dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=100 skip=1000 || error_msg "dd fail"
echo "dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=100 seek=1000"
dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=100 seek=1000 || error_msg "dd fail"
echo
echo "----- Finish -----"
