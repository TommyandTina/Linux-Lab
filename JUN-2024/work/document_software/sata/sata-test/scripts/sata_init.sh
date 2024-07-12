#!/bin/bash

echo "i2cset -y -f 4 0x20 0x02 0x00"
i2cset -y -f 4 0x20 0x02 0x00
echo "i2cset -y -f 4 0x20 0x03 0x7f"
i2cset -y -f 4 0x20 0x03 0x7f
echo "i2cset -y -f 4 0x20 0x01 0x7f"
i2cset -y -f 4 0x20 0x01 0x7f

MOD_PATH=/lib/modules/`uname -r`/kernel/drivers/ata
echo "lsmod | grep sata_rcar"
lsmod | grep sata_rcar
if [ $? != 0 ]; then
	echo "insmod $MOD_PATH/sata_rcar.ko"
	insmod $MOD_PATH/sata_rcar.ko
else
	echo "sata_rcar.ko is already installed"
fi
