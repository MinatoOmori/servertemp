#!/bin/bash

filename=`date +%m%d%H%M`_temperature.txt
touch $filename
echo time>$filename
./auto_oak.expect |grep DeviceID|awk -F '=' '{print $2}' >>$filename
while :
	do
		date +"%Y-%m-%d %H:%M:%S" >>$filename
		./auto_oak.expect |grep Curr|awk -F '=' '{print $2}' >>$filename
		sleep 1
	done
