#!/usr/bin/env python
#coding:utf-8

import sys
import re

original = sys.argv[1]
mod = original.replace("txt", "csv")

with open(original) as lines:
	with open(mod, mode='a') as of:
		i=0
		for line in lines:
			i+=1
			if i%45==0:
				of.write(line)
			else:
				text = line.rstrip('\r\n')
				of.write(text)
				of.write(',')
