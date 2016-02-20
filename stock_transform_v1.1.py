#coding:utf-8
#日线数据清洗,合并为一个文件，方便导入

import os
dir = "E:\\Project\\Python\\download2"
all_file = dir + "\\" + "all.csv"
try:
	all_f = open(all_file,"w")
except:
	print all_file + ' open fail'
	exit(-1)
for file in os.listdir(dir):
	old_file = dir + "\\" +file
	print old_file
	if os.path.isfile(old_file):
		try:
			old_f = open(old_file, 'r')
		except:
			print old_f + ' open fail'
			exit(-1)
		try:
			old_f_line = old_f.readline()
			while old_f_line != "":
				#添加该日期数据的归属股票编号
				if  old_f_line != "Date,Open,High,Low,Close,Volume,Adj Close\n":
					#all_f.write(os.path.splitext(file)[0].split('_')[1] + ',' + old_f_line)
					all_f.write(old_f_line)
				old_f_line = old_f.readline()
		except:
			print old_f + ' read fail'
		finally:
			old_f.close()
		print old_file + ' in'
all_f.close()		
print all_file		