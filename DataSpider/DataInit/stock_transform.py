#coding:utf-8
#日线数据清洗,方便导入,颠倒数据顺序

import os
dir_old = "E:/Project/Python/STOCK/DataSpider/DataUpdate/download"
dir_new = "E:/Project/Python/STOCK/DataSpider/DataUpdate/download2"

for file in os.listdir(dir_old):
	old_file = dir_old + "/" +file
	new_file = dir_new + "/" +file
	print old_file
	if os.path.isfile(old_file):
		try:
			old_f = open(old_file, 'r')
		except:
			print old_f + ' open fail'
			exit(-1)
		try:
			new_f = open(new_file,"w")
		except:
			print new_file + ' open fail'
			exit(-1)
		templist = []
		try:
			old_f_line = old_f.readline()
			while old_f_line != "":
				#添加该日期数据的归属股票编号
				if  old_f_line != "date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover\n":
					templist.append(old_f_line)
				old_f_line = old_f.readline()
			while len(templist)>0:
				new_f.write(templist.pop())
				
		except:
			print str(old_f) + ' read fail'
		finally:
			old_f.close()
			new_f.close()
		print str(old_file) + ' in'
		
print new_file		