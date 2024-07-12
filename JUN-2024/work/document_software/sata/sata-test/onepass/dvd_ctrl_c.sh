#!/usr/bin/expect

set timeout 5
spawn dd if=/dev/sr0 of=./dmy_10m bs=2048 count=5120 iflag=direct
sleep 1
send "\003\n"
interact
