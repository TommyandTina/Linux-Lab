#!/bin/bash

echo "Enable for SATA"
i2cset -y -f 4 0x20 0x02 0x00
i2cset -y -f 4 0x20 0x03 0x7f
i2cset -y -f 4 0x20 0x01 0x7f
insmod sata_rcar.ko

