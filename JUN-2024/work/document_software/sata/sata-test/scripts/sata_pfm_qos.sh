#!/bin/bash
#
usage()
{
cat << EOF
usage: `basename $0` [-xs] <qos_file>
	-xs: Salvator-XS
	qos_file: QoS cvs file

	Ex)
	`basename $0` -xs foo.csv
EOF
}

##### include #####
. `dirname $0`/sata_common.func

##### argument #####
QOS_FILE=""
_salvator_xs=0
while [ $# -gt 0 ]; do
	case "$1" in
		-xs)
			_salvator_xs=1
			;;
		*.csv)
			QOS_FILE=$1
			;;
		*)
			usage
			exit 1
			;;
	esac
	shift
done

if [ "X$QOS_FILE" == "X" ] ; then
	usage
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
echo "3.1 Performance Test No.3"
echo

# QoS setting
echo "modprobe qos"
modprobe qos || error_msg "modprobe qos fail"
echo "qos_tp setall $QOS_FILE"
qos_tp setall $QOS_FILE || error_msg "qos_tp fail"
echo "qos_tp switch"
qos_tp switch || error_msg "qos_tp fail"

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
