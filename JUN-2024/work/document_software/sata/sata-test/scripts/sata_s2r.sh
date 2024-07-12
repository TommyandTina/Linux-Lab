#!/bin/bash

usage()
{
cat << EOF
	usage: `basename $0` [-xs] [-f] <Test Number>
	-xs: Salvator-XS
	-f: format before test
	Test Number: 1 to 12

	Ex)
	`basename $0` -xs 1
EOF
}

##### include #####
. `dirname $0`/sata_common.func

##### argument #####
if [ $# == 0 ]; then
	usage
	exit 1
fi

_test_num=""
_salvator_xs=0
_format=0
while [ $# -gt 0 ]; do
	case "$1" in
		-xs)
			_salvator_xs=1
			;;
		-f)
			_format=1
			;;
		[1-9]*)
			_test_num=$1
			;;
		*)
			usage
			exit 1
			;;
	esac
	shift
done

echo "_test_num=$_test_num"
echo "_salvator_xs=$_salvator_xs"
echo "_format=$_format"

if [ "X$_test_num" == "X" ] ; then
	usage
	exit 1
fi

##### main #####
DATA_DIR=../data
FILE=f128m.txt

s2r_operation() {
	echo "i2cset -f -y 7 0x30 0x20 0x0F"
	i2cset -f -y 7 0x30 0x20 0x0F

	echo "Plase Turn switch SW23 to OFF (ON -> OFF)."
	echo "(Hit any key to next step)"
	read

	echo "After 10 second, Turn switch SW23 to ON (OFF -> ON)"
	sleep 1
	echo mem > /sys/power/state

	# wait rootfs wakeup
	cat /dev/null
}

if [ $_test_num == "1" ]; then
	echo "2.6 Suspend to RAM test No.1"
	echo
	echo "i2cset -f -y 7 0x30 0x20 0x0F"
	
	# Suspend and Resume
	s2r_operation

	# Module Install
	if [ ${_salvator_xs} == 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	# format
	if [ ${_format} == 1 ]; then
		echo "mkfs.ext4 -F /dev/sda1"
		mkfs.ext4 -F /dev/sda1 || error_msg "mkfs fail"
	fi

	echo "mkdir -p /mnt/sata"
	mkdir -p /mnt/sata || error_msg "mkdir fail"
	echo "mount /dev/sda1 /mnt/sata"
	mount /dev/sda1 /mnt/sata || error_msg "mount fail"

	echo "cp $DATA_DIR/$FILE /mnt/sata"
	cp $DATA_DIR/$FILE /mnt/sata || error_msg "cp fail"

	echo "cmp $DATA_DIR/$FILE /mnt/sata/$FILE"
	cmp $DATA_DIR/$FILE /mnt/sata/$FILE || error_msg "compare fail"

	echo "umount /mnt/sata"
	umount /mnt/sata || error_msg "umount fail"
	echo "rmdir /mnt/sata"
	rmdir /mnt/sata || error_msg "rmdif fail"
fi

if [ $_test_num == "2" ]; then
	if [ ${_salvator_xs} -eq 1 ]; then
		echo "**** Salvator-XS: Skip No.2 ****"
	else
		echo
		echo "2.6 Suspend to RAM test No.2"
		echo

		if [ ${_format} == 1 ]; then
			echo "mkfs.ext4 -F /dev/sda1"
			mkfs.ext4 -F /dev/sda1 || error_msg "mkfs fail"
		fi

		echo "mkdir -p /mnt/sata"
		mkdir -p /mnt/sata || error_msg "mkdir fail"
		echo "mount /dev/sda1 /mnt/sata"
		mount /dev/sda1 /mnt/sata || error_msg "mount fail"

		echo "cp $DATA_DIR/$FILE /mnt/sata/ &"
		cp $DATA_DIR/$FILE /mnt/sata/ &
		pid=$!

		# Suspend and Resume
		s2r_operation

		# wait for command completion before S2R
		echo "jobs"
		jobs
		echo "wait $pid"
		wait $pid
		sleep 1
		echo "sync"
		sync

		echo "cmp $DATA_DIR/$FILE /mnt/sata/$FILE"
		cmp $DATA_DIR/$FILE /mnt/sata/$FILE || error_msg "compare fail"

		echo "umount /mnt/sata"
		umount /mnt/sata || error_msg "umount fail"
		echo "rmdir /mnt/sata"
		rmdir /mnt/sata || error_msg "rmdif fail"
	fi
fi

if [ $_test_num == "3" ]; then
	if [ ${_salvator_xs} -eq 1 ]; then
		echo "**** Salvator-XS: Skip No.3 ****"
	else
		echo
		echo "2.6 Suspend to RAM test No.3"
		echo

		echo "cat /sys/kernel/debug/clk/sata0/clk_rate"
		cat /sys/kernel/debug/clk/sata0/clk_rate

		if [ ${_format} == 1 ]; then
			echo "mkfs.ext4 -F /dev/sda1"
			mkfs.ext4 -F /dev/sda1 || error_msg "mkfs fail"
		fi

		echo "mkdir -p /mnt/sata"
		mkdir -p /mnt/sata || error_msg "mkdir fail"
		echo "mount /dev/sda1 /mnt/sata"
		mount /dev/sda1 /mnt/sata || error_msg "mount fail"

		echo "cp $DATA_DIR/$FILE /mnt/sata/ &"
		cp $DATA_DIR/$FILE /mnt/sata/ &
		pid=$!

		# Suspend and Resume
		s2r_operation

		# wait for command completion before S2R
		echo "jobs"
		jobs
		echo "wait $pid"
		wait $pid
		sleep 1
		echo "sync"
		sync

		echo "cat /sys/kernel/debug/clk/sata0/clk_rate"
		cat /sys/kernel/debug/clk/sata0/clk_rate

		echo "umount /mnt/sata"
		umount /mnt/sata || error_msg "umount fail"
		echo "rmdir /mnt/sata"
		rmdir /mnt/sata || error_msg "rmdif fail"
	fi
fi

if [ $_test_num == "4" ]; then
	echo
	echo "2.6 Suspend to RAM test No.4"
	echo

	# Module Install
	if [ ${_salvator_xs} == 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	echo "cat /sys/kernel/debug/clk/sata0/clk_rate"
	cat /sys/kernel/debug/clk/sata0/clk_rate

	# Uninstall
	if [ ${_salvator_xs} == 1 ]; then
		echo "rmmod sata_rcar"
		rmmod sata_rcar || error_msg "rmmod fail"
	fi

	# Suspend and Resume
	s2r_operation

	# Module Install
	if [ ${_salvator_xs} -eq 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	echo "cat /sys/kernel/debug/clk/sata0/clk_rate"
	cat /sys/kernel/debug/clk/sata0/clk_rate
fi

if [ $_test_num == "5" ]; then
	echo
	echo "2.6 Suspend to RAM test No.5"
	echo

	# Module Install
	if [ ${_salvator_xs} == 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	echo "time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000"
	time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000
	echo "time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000"
	time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000

	# Uninstall
	if [ ${_salvator_xs} == 1 ]; then
		sleep 1
		echo "rmmod sata_rcar"
		rmmod sata_rcar || error_msg "rmmod fail"
	fi

	# Suspend and Resume
	s2r_operation

	# Module Install
	if [ ${_salvator_xs} -eq 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	echo "time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000"
	time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000
	echo "time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000"
	time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000

	echo "***** FileSystem may have been broken by this test. Please format. *****"

fi

if [ $_test_num == "6" ]; then
	if [ ${_salvator_xs} -eq 1 ]; then
		echo "**** Salvator-XS: Skip No.6 ****"
	else
		echo
		echo "2.6 Suspend to RAM test No.6"
		echo

		echo "time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000"
		time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000
		echo "time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000"
		time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000

		echo "dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000 &"
		dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000 &
		pid=$!

		# Suspend and Resume
		s2r_operation

		# wait for command completion before S2R
		echo "jobs"
		jobs
		echo "wait $pid"
		wait $pid
		sleep 1
		echo "sync"
		sync

		echo "time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000"
		time dd iflag=direct if=/dev/sda1 of=/dev/null bs=1M count=1024 skip=1000
		echo "time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000"
		time dd oflag=direct if=/dev/zero of=/dev/sda1 bs=1M count=1024 seek=1000

		echo "***** FileSystem may have been broken by this test. Please format. *****"
	fi
fi

if [ $_test_num == "7" ]; then

	echo
	echo "2.6 Suspend to RAM test No.7"
	echo

	# Suspend and Resume
	s2r_operation

	# Module install
	if [ ${_salvator_xs} == 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	echo "mkdir -p /mnt/sata"
	mkdir -p /mnt/sata || error_msg "mkdir fail"
	echo "mount /dev/sr0 /mnt/sata"
	mount /dev/sr0 /mnt/sata || error_msg "mount fail"

	echo "cp /mnt/sata/md5sum.txt ./"
	cp /mnt/sata/md5sum.txt ./ || error_msg "cp fail"

	echo "cmp /mnt/sata/md5sum.txt ./md5sum.txt"
	cmp /mnt/sata/md5sum.txt ./md5sum.txt || error_msg "compare fail"

	echo "rm ./md5sum.txt"
	rm ./md5sum.txt || error_msg "rm fail"

	echo sync
	sync
	echo "umount /mnt/sata"
	umount /mnt/sata || error_msg "umount fail"
	echo "rmdir /mnt/sata"
	rmdir /mnt/sata || error_msg "rmdif fail"
fi

if [ $_test_num == "8" ]; then
	if [ ${_salvator_xs} -eq 1 ]; then
		echo "**** Salvator-XS: Skip No.8 ****"
	else
		echo
		echo "2.6 Suspend to RAM test No.8"
		echo

		echo "dd iflag=direct if=/dev/sr0 of=/dev/null bs=2048 count=1024 &"
		dd iflag=direct if=/dev/sr0 of=/dev/null bs=2048 count=1024 &
		pid=$!

		# Suspend and Resume
		s2r_operation

		# wait for command completion before S2R
		echo "jobs"
		jobs
		echo "wait $pid"
		wait $pid
		sleep 1
		echo "sync"
		sync

		echo "mkdir -p /mnt/sata"
		mkdir -p /mnt/sata || error_msg "mkdir fail"
		echo "mount /dev/sr0 /mnt/sata"
		mount /dev/sr0 /mnt/sata || error_msg "mount fail"

		echo "cp /mnt/sata/md5sum.txt ./"
		cp /mnt/sata/md5sum.txt ./ || error_msg "cp fail"

		echo "cmp /mnt/sata/md5sum.txt ./md5sum.txt"
		cmp /mnt/sata/md5sum.txt ./md5sum.txt || error_msg "compare fail"

		echo "rm ./md5sum.txt"
		rm ./md5sum.txt || error_msg "rm fail"

		echo sync
		sync
		echo "umount /mnt/sata"
		umount /mnt/sata || error_msg "umount fail"
		echo "rmdir /mnt/sata"
		rmdir /mnt/sata || error_msg "rmdif fail"
	fi
fi

if [ $_test_num == "9" ]; then
	if [ ${_salvator_xs} -eq 1 ]; then
		echo "**** Salvator-XS: Skip No.9 ****"
	else
		echo
		echo "2.6 Suspend to RAM test No.9"
		echo

		echo "cat /sys/kernel/debug/clk/sata0/clk_rate"
		cat /sys/kernel/debug/clk/sata0/clk_rate

		echo "dd iflag=direct if=/dev/sr0 of=/dev/null bs=2048 count=1024 &"
		dd iflag=direct if=/dev/sr0 of=/dev/null bs=2048 count=1024 &
		pid=$!

		# Suspend and Resume
		s2r_operation

		# wait for command completion before S2R
		echo "jobs"
		jobs
		echo "wait $pid"
		wait $pid
		sleep 1

		echo "cat /sys/kernel/debug/clk/sata0/clk_rate"
		cat /sys/kernel/debug/clk/sata0/clk_rate
	fi
fi

if [ $_test_num == "10" ]; then
	echo
	echo "2.6 Suspend to RAM test No.10"
	echo

	# Module install
	if [ ${_salvator_xs} == 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	echo "cat /sys/kernel/debug/clk/sata0/clk_rate"
	cat /sys/kernel/debug/clk/sata0/clk_rate

	# Uninstall
	if [ ${_salvator_xs} == 1 ]; then
		echo "sleep 3"
		sleep 3
		echo "rmmod sata_rcar"
		rmmod sata_rcar || error_msg "rmmod fail"
	fi

	# Suspend and Resume
	s2r_operation

	# Module install
	if [ ${_salvator_xs} == 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	echo "cat /sys/kernel/debug/clk/sata0/clk_rate"
	cat /sys/kernel/debug/clk/sata0/clk_rate
fi

if [ $_test_num == "11" ]; then
	echo
	echo "2.6 Suspend to RAM test No.11"
	echo

	# Module install
	if [ ${_salvator_xs} == 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	echo "time dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512"
	time dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512

	# Uninstall
	if [ ${_salvator_xs} == 1 ]; then
		echo "sleep 3"
		sleep 3
		echo "rmmod sata_rcar"
	fi

	# Suspend and Resume
	s2r_operation

	# Module install
	if [ ${_salvator_xs} == 1 ]; then
		echo "Initialize for Salvator-XS"
		sata_start_i2c
		sata_module_install "INSMOD"
	fi

	echo "time dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512"
	time dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512
fi

if [ $_test_num == "12" ]; then
	if [ ${_salvator_xs} == 1 ]; then
		echo "**** Salvator-XS: Skip No.12 ****"
	else
		echo
		echo "2.6 Suspend to RAM test No.12"
		echo

		echo "time dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512"
		time dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512

		echo "dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512 &"
		dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512 &
		pid=$!

		# Suspend and Resume
		s2r_operation

		# wait for command completion before S2R
		echo "jobs"
		jobs
		echo "wait $pid"
		wait $pid
		sleep 1

		echo "time dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512"
		time dd iflag=direct if=/dev/sr0 of=/dev/null bs=1M count=512
	fi
fi

echo "----- Finish -----"
