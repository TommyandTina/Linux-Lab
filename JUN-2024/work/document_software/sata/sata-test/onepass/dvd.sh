#!/bin/bash

TESTCOUNT=0
INCOUNT=0

echo "------------------------------------------------------"
echo -e "*** SATA DVD Onepass Test Start. ***\n"

echo "-- Normal Test No.16 --"
echo "dmesg | grep ata1"
dmesg | grep ata1
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "dmesg | grep scsi"
dmesg | grep scsi
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "dmesg | grep CD-ROM"
dmesg | grep CD-ROM
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

if [ $INCOUNT -eq 3 ]; then
	echo -e "*** Normal Test No.16 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.16 Fail. ***\n"
fi

INCOUNT=0
sleep 2

echo "------------------------------------------------------"
echo "-- Normal Test No.17 --"
echo "ls /dev/sr*"
ls /dev/sr*
if [ $? -eq 0 ]; then
	echo -e "*** Normal Test No.17 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.17 Fail. ***\n"
fi

sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.18 --"
echo "mkdir /mnt/sata"
mkdir -p /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sr0 /mnt/sata"
mount /dev/sr0 /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "ls /mnt/sata"
ls /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

if [ $INCOUNT -eq 3 ]; then
	echo -e "*** Normal Test No.18 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.18 Fail. ***\n"
fi

INCOUNT=0
sleep 2

echo "------------------------------------------------------"
echo "-- Normal Test No.19 --"

echo "sync"
sync
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "umount /mnt/sata"
umount /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "ls /mnt/sata"
ls /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rmdir /mnt/sata"
rmdir /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

if [ $INCOUNT -eq 4 ]; then
	echo -e "*** Normal Test No.19 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.19 Fail. ***\n"
fi

INCOUNT=0
sleep 2

echo "------------------------------------------------------"
echo "-- Normal Test No.20 --"

echo "mkdir /mnt/sata"
mkdir -p /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sr0 /mnt/sata"
mount /dev/sr0 /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "ls /mnt/sata"
ls /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "cp /mnt/sata/md5sum.txt ./"
cp /mnt/sata/md5sum.txt ./
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "diff md5sum.txt /mnt/sata/md5sum.txt"
diff md5sum.txt /mnt/sata/md5sum.txt
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rm md5sum.txt"
rm md5sum.txt
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "sync"
sync
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "umount /mnt/sata"
umount /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rmdir /mnt/sata"
rmdir /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

if [ $INCOUNT -eq 9 ]; then
	echo -e "*** Normal Test No.20 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.20 Fail. ***\n"
fi

INCOUNT=0
sleep 2

echo "------------------------------------------------------"
echo "-- Normal Test No.21 --"

echo "dd if=/dev/sr0 of=/dev/null bs=2048 count=1 skip=175198"
dd if=/dev/sr0 of=/dev/null bs=2048 count=1 skip=175198
if [ $? -eq 0 ]; then
	echo -e "*** Normal Test No.21 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.21 Fail. ***\n"
fi

sleep 2

echo "------------------------------------------------------"
echo "-- Normal Test No.22 --"

echo "mkdir /mnt/sata"
mkdir -p /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sr0 /mnt/sata"
mount /dev/sr0 /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "./dvd_ctrl_c.sh"
./dvd_ctrl_c.sh
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "dd if=/dev/sr0 of=./dmy_10m bs=2048 count=5120 iflag=direct"
dd if=/dev/sr0 of=./dmy_10m bs=2048 count=5120 iflag=direct
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "ls -alh | grep dmy_10m"
ls -alh | grep dmy_10m
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rm dmy_10m"
rm dmy_10m
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "sync"
sync
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "umount /mnt/sata"
umount /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rmdir /mnt/sata"
rmdir /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

if [ $INCOUNT -eq 9 ]; then
	echo -e "*** Normal Test No.22 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.22 Fail. ***\n"
fi

INCOUNT=0
sleep 2

echo "------------------------------------------------------"
echo "-- Normal Test No.23 --"

echo "mkdir /mnt/sata"
mkdir /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sr0 /mnt/sata"
mount /dev/sr0 /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "./dvd_ctrl_z.sh"
./dvd_ctrl_z.sh
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "ls -alh | grep dmy_10m"
ls -alh | grep dmy_10m
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rm dmy_10m"
rm dmy_10m
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "sync"
sync
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "umount /mnt/sata"
umount /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rmdir /mnt/sata"
rmdir /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

if [ $INCOUNT -eq 8 ]; then
	echo -e "*** Normal Test No.23 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.23 Fail. ***\n"
fi

INCOUNT=0
sleep 2

echo "------------------------------------------------------"
if [ $TESTCOUNT -eq 8 ]; then
	echo -e "*** SATA DVD Onepass Test is All Passed! ***\n"
else
	echo -e "*** SATA DVD Onepass Test is Failed. ***\n"
fi
