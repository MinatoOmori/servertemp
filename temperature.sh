#!/bin/bash

filename=`date +%m%d%H%M`_temperature.txt
touch $filename
echo time>$filename
./auto_oak.expect |grep DeviceID|awk -F '=' '{print $2}' >>$filename
while :
	do
		date +%H:%M:%S.%3N >>$filename
		./auto_oak.expect |grep Curr|awk -F '=' '{print $2}' >>$filename
	done
