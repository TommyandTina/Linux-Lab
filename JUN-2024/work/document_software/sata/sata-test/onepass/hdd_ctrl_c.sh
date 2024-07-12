#!/usr/bin/expect

set timeout 5
spawn dd if=/dev/zero of=/mnt/sata/dmy_100M bs=512 count=204800
sleep 1
send "\003\n"
interact
