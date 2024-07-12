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
echo
echo "3.1 Performance Test No.1"
echo

echo "Read Performance:"
echo
echo "for (( c=1; c<=5; c++ )); do time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000; done"
for (( c=1; c<=5; c++ )); do time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000; done
echo

echo "Write Performance:"
echo
echo "for (( c=1; c<=5; c++ )); do time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000; done"
for (( c=1; c<=5; c++ )); do time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000; done
echo
echo "Target performance value"
echo " Read  : 221 MB/s"
echo " write : 185 MB/s"

echo "----- Finish -----"
