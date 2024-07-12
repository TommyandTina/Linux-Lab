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

##### Salvator-XS #####
if [ ${_salvator_xs} -eq 1 ]; then
        echo "Initialize for Salvator-XS"
        sata_start_i2c
fi

echo
echo "2.4 Modularization Test No.1"
echo

sata_module_install "INSMOD"

echo "lsmod"
lsmod

echo "mkdir -p /mnt/sata"
mkdir -p /mnt/sata || error_msg "mkdir fail"

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata || error_msg "mount fail"

echo "echo test > test.txt"
echo test > test.txt || error_msg "create test.txt fail"

echo "cp test.txt /mnt/sata"
cp test.txt /mnt/sata || error_msg "cp fail"
echo "sync"
sync

echo "cmp test.txt /mnt/sata/test.txt"
cmp test.txt /mnt/sata/test.txt || error_msg "compare fail"

echo "umount /mnt/sata"
umount /mnt/sata || error_msg "mount fail"
echo "rmdir /mnt/sata"
rmdir /mnt/sata || error_msg "rmdir fail"

echo
echo "2.4 Modularization Test No.2"
echo

echo "rmmod sata_rcar"
rmmod sata_rcar || error_msg "rmmod error"

echo "lsmod"
lsmod

echo "lsmod | grep sata_rcar"
lsmod | grep sata_rcar && error_msg "lsmod fail"
echo "Pass: Not found sata_rcar.ko"

echo
echo "2.4 Modularization Test No.3"
echo

sata_module_install "INSMOD"

echo "lsmod"
lsmod

echo "lsmod | grep sata_rcar"
lsmod | grep sata_rcar || error_msg "lsmod fail"

echo "mkdir -p /mnt/sata"
mkdir -p /mnt/sata || error_msg "mkdir fail"
echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata || error_msg "mount fail"

echo "cp /mnt/sata/test.txt test1.txt"
cp /mnt/sata/test.txt test1.txt || error_msg "cp fail"

echo "sync"
sync

echo "cmp test.txt test1.txt"
cmp test.txt test1.txt || error_msg "compare fail"

echo "rm test.txt test1.txt /mnt/sata/test.txt"
rm test.txt test1.txt /mnt/sata/test.txt || error_msg "rm fail"
echo "sync"
sync
echo "umount /mnt/sata"
umount /mnt/sata || error_msg "umount fail"
echo
echo "rmdir /mnt/sata"
rmdir /mnt/sata || error_msg "rmdir fail"

echo "----- Finish -----"
