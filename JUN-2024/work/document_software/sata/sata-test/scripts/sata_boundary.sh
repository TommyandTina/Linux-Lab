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
		HDD)
			TARGET=$1
			DEVFILE=/dev/sda
			;;
		DVD)
			TARGET=$1
			DEVFILE=/dev/sr0
			;;
		*)
			usage
			exit 1
			;;
	esac
	shift
done

#echo "TARGET=$TARGET"
#echo "_salvator_xs=$_salvator_xs"

if [ "X$TARGET" == "X" ] ; then
	echo "Select HDD or DVD"
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
SECNUM=`fdisk -lu $DEVFILE | grep sectors$ | awk '{print $7}'`

echo "SECNUM=$SECNUM"
echo "fdisk -lu $DEVFILE"
fdisk -lu $DEVFILE

LASTSEC=`expr $SECNUM - 1`
echo "LASTSEC=$LASTSEC"

if [ $DEVFILE == "/dev/sda" ] ; then

	echo
	echo "2.3 Boundary Value Test No.1"
	echo

	echo "dd if=/dev/zero of=$DEVFILE bs=512 count=1"
	dd if=/dev/zero of=$DEVFILE bs=512 count=1 || error_msg "write fail"

	echo
	echo "2.3.Boundary Value Test No.2"
	echo

	echo "dd if=$DEVFILE of=/dev/null bs=512 count=1"
	dd if=$DEVFILE of=/dev/null bs=512 count=1 || error_msg "read fail"

	echo
	echo "2.3.Boundary Value Test No.3"
	echo

	echo "dd if=/dev/zero of=$DEVFILE bs=512 count=1 seek=$LASTSEC"
	dd if=/dev/zero of=$DEVFILE bs=512 count=1 seek=$LASTSEC || error_msg "write last fail"

	echo
	echo "2.3.Boundary Value Test No.4"
	echo

	echo "dd if=$DEVFILE of=/dev/null bs=512 count=1 skip=$LASTSEC"
	dd if=$DEVFILE of=/dev/null bs=512 count=1 skip=$LASTSEC || error_msg "Read last fail"

	echo
	echo "2.3.Boundary Value Test No.5"
	echo

	echo "dd if=/dev/zero of=$DEVFILE bs=512 count=1 seek=$SECNUM"
	dd if=/dev/zero of=$DEVFILE bs=512 count=1 seek=$SECNUM && error_msg "Write last sector+1 succeeded"

	echo
	echo "2.3.Boundary Value Test No.6"
	echo

	echo "dd if=$DEVFILE of=/dev/null bs=512 count=1 skip=$SECNUM"
	dd if=$DEVFILE of=/dev/null bs=512 count=1 skip=$SECNUM || error_msg "read last+1 fail"
	echo "***** Expect: Read size = 0bytes *****"

	echo
	echo "2.3.Boundary Value Test No.7"
	echo

	echo "dd if=/dev/zero of=$DEVFILE bs=512 count=2 seek=$LASTSEC"
	dd if=/dev/zero of=$DEVFILE bs=512 count=2 seek=$LASTSEC && error_msg "Write last sector+1 succeeded"

	echo
	echo "2.3.Boundary Value Test No.8"
	echo

	echo "dd if=$DEVFILE of=/dev/null bs=512 count=2 skip=$LASTSEC"
	dd if=$DEVFILE of=/dev/null bs=512 count=2 skip=$LASTSEC || error_msg "2blocks read fail"
	echo "***** Expect: Read size = 512bytes *****"

	echo
	echo "Partition table was deleted by test."
	echo "Format"
	sata_fdisk || error_msg "fdisk fail"
	DEVFILE=/dev/sda1
	echo "mkfs.ext4 -F $DEVFILE"
	mkfs.ext4 -F $DEVFILE || error_msg "mkfs fail"

	echo
	echo "2.3 Boundary Value Test No.9"
	echo

	echo "mkdir -p /mnt/sata"
	mkdir -p /mnt/sata || error_msg "mkdir fail"

	echo "mount "$DEVFILE" /mnt/sata"
	mount $DEVFILE /mnt/sata || error_msg "mount fail"

	echo "touch /tmp/0byte.txt"
	touch /tmp/0byte.txt || error_msg "create 0byte file fail"

	echo "cp /tmp/0byte.txt /mnt/sata/0byte_w.txt"
	cp /tmp/0byte.txt /mnt/sata/0byte_w.txt || error_msg "Write 0byte file fail"
	echo "sync"
	sync
	echo "cp /mnt/sata/0byte_w.txt /tmp/0byte_r.txt"
	cp /mnt/sata/0byte_w.txt /tmp/0byte_r.txt || error_msg "Read 0byte file fail"

	echo "diff /tmp/0byte.txt /tmp/0byte_r.txt"
	diff /tmp/0byte.txt /tmp/0byte_r.txt || error_msg "compare fail"

	echo "rm /tmp/0byte.txt /tmp/0byte_r.txt /mnt/sata/0byte_w.txt"
	rm /tmp/0byte.txt /tmp/0byte_r.txt /mnt/sata/0byte_w.txt || error_msg "rm fail"
	echo "sync"
	sync

	echo "umount /mnt/sata"
	umount /mnt/sata || error_msg "umount fail"
	echo "rmdir /mnt/sata"
	rmdir /mnt/sata || error_msg "rmdir fail"

	echo
	echo "2.3 Boundary Value Test No.10"
	echo

	echo "mkdir -p /mnt/sata"
	mkdir -p /mnt/sata || error_msg "mkdir fail"

	echo "mount $DEVFILE /mnt/sata"
	mount $DEVFILE /mnt/sata || error_msg "mount fail"

	echo "echo > /tmp/1byte.txt"
	echo > /tmp/1byte.txt || error_msg "create 1byte file fail"

	echo "cp /tmp/1byte.txt /mnt/sata/1byte_w.txt"
	cp /tmp/1byte.txt /mnt/sata/1byte_w.txt || error_msg "Write fail"
	echo "sync"
	sync

	echo "cp /mnt/sata/1byte_w.txt /tmp/1byte_r.txt"
	cp /mnt/sata/1byte_w.txt /tmp/1byte_r.txt || error_msg "Read fail"

	echo "diff /tmp/1byte.txt /tmp/1byte_r.txt"
	diff /tmp/1byte.txt /tmp/1byte_r.txt || error_msg "compare fail"

	echo "rm /tmp/1byte.txt /tmp/1byte_r.txt /mnt/sata/1byte_w.txt"
	rm /tmp/1byte.txt /tmp/1byte_r.txt /mnt/sata/1byte_w.txt || error_msg "rm fail"
	echo "sync"
	sync

	echo "umount /mnt/sata"
	umount /mnt/sata || error_msg "umount fail"
	echo "rmdir /mnt/sata"
	rmdir /mnt/sata || error_msg "rmdir fail"
else
	echo
	echo "2.3.Boundary Value Test No.11"
	echo
	echo "dd if=$DEVFILE of=/dev/null bs=2048 count=1"
	dd if=$DEVFILE of=/dev/null bs=2048 count=1 || error_msg "read 1st fail"

	echo
	echo "2.3.Boundary Value Test No.12"
	echo
	echo "dd if=$DEVFILE of=/dev/null bs=2048 count=1 skip=$LASTSEC"
	dd if=$DEVFILE of=/dev/null bs=2048 count=1 skip=$LASTSEC || error_msg "read last fail"

	echo
	echo "2.3.Boundary Value Test No.13"
	echo
	echo "dd if=$DEVFILE of=/dev/null bs=2048 count=1 skip=$SECNUM"
	dd if=$DEVFILE of=/dev/null bs=2048 count=1 skip=$SECNUM || error_msg "read last+1 fail"
	echo "**** Expect: Read size = 0bytes ****"

	echo
	echo "2.3.Boundary Value Test No.14"
	echo
	echo "dd if=$DEVFILE of=/dev/null bs=2048 count=2 skip=$LASTSEC"
	dd if=$DEVFILE of=/dev/null bs=2048 count=2 skip=$LASTSEC || error_msg "2blocks read fail"
	echo "***** Expect: Read size = 2048bytes *****"

fi

echo "----- Finish -----"
