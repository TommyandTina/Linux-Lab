#!/bin/bash

TESTCOUNT=0
INCOUNT=0

echo -e "*** SATA HDD Onepass Test Start. ***\n"
echo "------------------------------------------------------"
echo "-- Normal Test No.3 --"

echo "dmesg | grep sata_rcar"
dmesg | grep sata_rcar
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "dmesg | grep ata1"
dmesg | grep ata1
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "dmesg | grep sda"
dmesg | grep sda
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

if [ $INCOUNT -eq 3 ]; then
	echo -e "*** Normal Test No.3 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.3 Fail. ***\n"
fi

INCOUNT=0
sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.4 --"
echo "ls /dev/sd*"
ls /dev/sd*
if [ $? -eq 0 ]; then
	echo -e "*** Normal Test No.4 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.4 Fail. ***\n"
fi

sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.5 --"
echo "mkdir -p /mnt/sata"
mkdir -p /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata
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
	echo -e "*** Normal Test No.5 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.5 Fail. ***\n"
fi

INCOUNT=0
sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.6 --"

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
	echo -e "*** Normal Test No.6 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.6 Fail. ***\n"
fi

INCOUNT=0
sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.7 --"

echo "mkdir /mnt/sata"
mkdir -p /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "echo test > test.txt"
echo test > test.txt
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "cp test.txt /mnt/sata"
cp test.txt /mnt/sata
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

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata
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

echo "diff test.txt /mnt/sata/test.txt"
diff test.txt /mnt/sata/test.txt
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rm test.txt /mnt/sata/test.txt"
rm test.txt /mnt/sata/test.txt
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

if [ $INCOUNT -eq 13 ]; then
	echo -e "*** Normal Test No.7 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.7 Fail. ***\n"
fi

INCOUNT=0
sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.8 --"

echo "mkdir /mnt/sata"
mkdir -p /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "echo test > /mnt/sata/test.txt"
echo test > /mnt/sata/test.txt
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "cp /mnt/sata/test.txt /mnt/sata/test2.txt"
cp /mnt/sata/test.txt /mnt/sata/test2.txt
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

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata
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

echo "diff /mnt/sata/test.txt /mnt/sata/test2.txt"
diff /mnt/sata/test.txt /mnt/sata/test2.txt
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rm /mnt/sata/test.txt /mnt/sata/test2.txt"
rm /mnt/sata/test.txt /mnt/sata/test2.txt
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

if [ $INCOUNT -eq 13 ]; then
	echo -e "*** Normal Test No.8 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.8 Fail. ***\n"
fi

INCOUNT=0
sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.9 --"

echo "dd if=/dev/zero of=/dev/sda1 bs=512 count=1 seek=117220824"
dd if=/dev/zero of=/dev/sda1 bs=512 count=1 seek=117220824
if [ $? -eq 0 ]; then
	echo -e "*** Normal Test No.9 Pass! ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.9 Fail. ***\n"
fi
sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.10 --"

echo "mkdir /mnt/sata"
mkdir -p /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "echo test > /mnt/sata/test.txt"
echo test > /mnt/sata/test.txt
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "cp /mnt/sata/test.txt ./"
cp /mnt/sata/test.txt ./
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

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata
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

echo "diff test.txt /mnt/sata/test.txt"
diff test.txt /mnt/sata/test.txt
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rm test.txt /mnt/sata/test.txt"
rm test.txt /mnt/sata/test.txt
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

if [ $INCOUNT -eq 13 ]; then
	echo -e "*** Normal Test No.10 is Passed! ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.10 is Failed. ***\n"
fi

INCOUNT=0
sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.11 --"

echo "dd if=/dev/sda1 of=/dev/zero bs=512 count=1 skip=117220824"
dd if=/dev/sda1 of=/dev/zero bs=512 count=1 skip=117220824
if [ $? -eq 0 ]; then
	echo -e "*** Normal Test No.11 is Passed! ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.11 is Failed. ***\n"
fi

sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.12 --"

echo "mkdir /mnt/sata"
mkdir -p /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "./hdd_ctrl_c.sh"
./hdd_ctrl_c.sh
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "Check Data"
echo "du -h /mnt/sata/dmy_100M"
du -h /mnt/sata/dmy_100M
sleep 1

echo "Retry dd"
echo "dd if=/dev/zero of=/mnt/sata/dmy_100M bs=512 count=204800"
dd if=/dev/zero of=/mnt/sata/dmy_100M bs=512 count=204800
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "ls -alh /mnt/sata/dmy_100M"
ls -alh /mnt/sata/dmy_100M
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rm /mnt/sata/dmy_100M"
rm /mnt/sata/dmy_100M
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
	echo -e "*** Normal Test No.12 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.12 Fail. ***\n"
fi

INCOUNT=0
sleep 1

echo "------------------------------------------------------"
echo "-- Normal Test No.13 --"

echo "mkdir /mnt/sata"
mkdir -p /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "mount /dev/sda1 /mnt/sata"
mount /dev/sda1 /mnt/sata
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "./hdd_ctrl_z.sh"
./hdd_ctrl_z.sh
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "ls -alh /mnt/sata/dmy_1000M"
ls -alh /mnt/sata/dmy_1000M
if [ $? -eq 0 ]; then
	echo -e "Pass.\n"
	INCOUNT=$((INCOUNT+1))
else
	echo -e "Fail.\n"
fi
sleep 1

echo "rm /mnt/sata/dmy_1000M"
rm /mnt/sata/dmy_1000M
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
	echo -e "*** Normal Test No.13 Pass. ***\n"
	TESTCOUNT=$((TESTCOUNT+1))
else
	echo -e "*** Normal Test No.13 Fail. ***\n"
fi

echo "------------------------------------------------------"
if [ $TESTCOUNT -eq 11 ]; then
	echo -e "*** SATA HDD Onepass Test is All Passed! ***\n"
else
	echo -e "*** SATA HDD Onepass Test is Failed. ***\n"
fi
