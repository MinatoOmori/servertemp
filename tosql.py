#!/usr/bin/env python
#coding:utf-8

import sys
import MySQLdb
import datetime
import numpy as np

original = sys.argv[1]

con = MySQLdb.connect(
	user='root',
	passwd='pass',
	host='njPi',
	db='oomori',
	charset='utf8'
	)
c = con.cursor()

with open(original) as lines:
	i=0
	values=[""]+[0]*75
	for line in lines:
		if i < 76:
			pass
		elif i%76==0:
			values[i%76]=line.rstrip()
		elif line=="N/A\n":
			values[i%76]="0"
		elif i%76==75:
			#values[i%51]=float(line)
			values[i%76]=line.rstrip()
			sql="INSERT INTO ilo4 VALUES" + "('" + values[0]+"',"+values[1]+","+values[2]+","+values[3]+","+values[4]+","+values[5]+","+values[6]+","+values[7]+","+values[8]+","+values[9]+","+values[10]+","+values[11]+","+values[12]+","+values[13]+","+values[14]+","+values[15]+","+values[16]+","+values[17]+","+values[18]+","+values[19]+","+values[20]+","+values[21]+","+values[22]+","+values[23]+","+values[24]+","+values[25]+","+values[26]+","+values[27]+","+values[28]+","+values[29]+","+values[30]+","+values[31]+","+values[32]+","+values[33]+","+values[34]+","+values[35]+","+values[36]+","+values[37]+","+values[38]+","+values[39]+","+values[40]+","+values[41]+","+values[42]+","+values[43]+","+values[44]+","+values[45]+","+values[46]+","+values[47]+","+values[48]+","+values[49]+","+values[50] + ");"
			c.execute(sql)
			sql="INSERT INTO lmsensors VALUES" + "('" + values[0]+"',"+values[51]+","+values[52]+","+values[53]+","+values[54]+","+values[55]+","+values[56]+","+values[57]+","+values[58]+","+values[59]+","+values[60]+","+values[61]+","+values[62]+","+values[63]+","+values[64]+","+values[65]+","+values[66]+","+values[67]+","+values[68]+");"
			c.execute(sql)
			sql="INSERT INTO usages VALUES" + "('" + values[0]+"',"+values[69]+","+values[70]+","+values[71]+","+values[72]+","+values[73]+","+values[74]+","+values[75]+");"
			c.execute(sql)
		else:
			values[i%76]=line.rstrip()
		i+=1

c.close()
con.commit()
con.close()

