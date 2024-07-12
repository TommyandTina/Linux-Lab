#!/bin/bash

SRC_FILE=/dev/sr0/f10m
DST_FILE=./dmy_10m

{
	echo "exec CTRL-Z after 2 seconds.."

	sleep 2

	pid=$(ps aux | grep -w 'dd' | grep dmy_10m | awk '{print $2}')
	echo "do SIGTSTP (CTRL-Z)...PID=${pid}"
	kill -TSTP $pid

	echo "check pause  copy process"
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 2
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 2
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 2

	echo "do SIGCONT...PID=${pid}"
	kill -CONT $pid

	echo "check unpause copy process"
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 2
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 2
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 2
} &

pid_ctrl_z=$!

echo "start dd"
echo "dd if=/dev/sr0 of=./dmy_10m bs=2048 count=5120 iflag=direct"
dd if=/dev/sr0 of=./dmy_10m bs=2048 count=5120 iflag=direct
echo "Wait for CTRL-Z process ${pid_ctrl_z}"
wait ${pid_ctrl_z}
echo "wait end"
