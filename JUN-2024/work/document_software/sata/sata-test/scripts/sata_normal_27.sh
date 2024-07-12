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
DATA_DIR=../data
FILE=f128m.txt

echo
echo "2.1.Normal System Test No.27"
echo

echo "dmesg | grep iommu"
dmesg | grep iommu

echo "mkdir -p /mnt/sata"
mkdir -p /mnt/sata || error_msg "mkdir fail"

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata || error_msg "mount fail"

echo "cp $DATA_DIR/$FILE /mnt/sata/."
cp $DATA_DIR/$FILE /mnt/sata/. || error_msg "cp fail"

echo "cmp $DATA_DIR/$FILE /mnt/sata/$FILE"
cmp $DATA_DIR/$FILE /mnt/sata/$FILE || error_msg "cmp fail"

echo sync
sync

echo "cp /mnt/sata/$FILE /tmp/$FILE"
cp /mnt/sata/$FILE /tmp/$FILE || error_msg "cp fail"

echo "cmp /mnt/sata/$FILE /tmp/$FILE"
cmp /mnt/sata/$FILE /tmp/$FILE || error_msg "cmp fail"

echo "rm /tmp/$FILE"
rm /tmp/$FILE || error_msg "rm /tmp/$FILE fail"

echo "sync"
sync
echo "umount /mnt/sata"
umount /mnt/sata
echo "rmdir /mnt/sata"
rmdir /mnt/sata
echo "----- Finish -----"
