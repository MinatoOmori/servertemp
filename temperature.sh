#!/bin/bash

filename=`date +%m%d%H%M`_temperature.txt
touch $filename
echo time>$filename
./auto_oak.expect |grep DeviceID|awk -F '=' '{print $2}' >>$filename
./auto_oak.expect |grep -e Physical -e Core |awk -F ':' '{print $1}' >>$filename
echo total reads>>$filename
echo writes>>$filename
echo merged writes>>$filename
echo used memory>>$filename
echo non-nice user cpu ticks>>$filename
echo nice user cpu ticks>>$filename
echo system cpu ticks>>$filename
while :
	do
		date +"%Y-%m-%d %H:%M:%S" >>$filename
		./auto_oak.expect |grep Curr|awk -F '=' '{print $2}' >>$filename
		./auto_oak.expect |grep Physical |awk -F '[°C+]' '{print $2}' >>$filename
		./auto_oak.expect |grep Core |awk -F '[°C+]' '{print $3}' >>$filename
		./auto_oak.expect |grep -e "total reads" -e writes -e "used memory" -e "non-nice user cpu ticks" -e "nice user cpu ticks" -e "system cpu ticks" |awk -F ' ' '{print $1}' >>$filename
		sleep 1
	done
