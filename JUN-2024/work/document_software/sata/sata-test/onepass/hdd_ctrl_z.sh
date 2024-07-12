#!/bin/bash

SRC_FILE=./dmy_1000M
DST_FILE=/mnt/sata/dmy_1000M

{
	echo "exec CTRL-Z after 5 seconds.."

	sleep 5

	pid=$(ps aux | grep -w 'dd' | grep ${DST_FILE} | awk '{print $2}')
	echo "do SIGTSTP (CTRL-Z)...PID=${pid}"
	kill -TSTP $pid

	echo "check pause copy process"
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 5
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 5
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 5

	echo "do SIGCONT...PID=${pid}"
	kill -CONT $pid

	echo "check unpause copy process"
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 5
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 5
	echo "${DST_FILE} is $(wc -c < ${DST_FILE})"
	sleep 5
} &

pid_ctrl_z=$!

echo "start dd"
echo "dd if=/dev/urandom of=${DST_FILE} bs=1M count=1024"
dd if=/dev/urandom of=${DST_FILE} bs=1M count=1024
echo "Wait for CTRL-Z process ($pid_ctrl_z)"
wait $pid_ctrl_z
echo "wait end"
