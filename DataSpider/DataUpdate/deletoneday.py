#coding:utf-8
#数据导入数据库
import MySQLdb
import os

def load(date):
	try:
		conn=MySQLdb.connect(host="localhost",user="root",db="stock_1.0")
		cur=conn.cursor()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])	
	dir = "E:/Project/Python/STOCK/DataSpider/DataUpdate/daily_update_d_download3"
	for file in os.listdir(dir):
		print dir + "/" +file
		if os.path.isfile(dir + "/" + file):
			#载入数据库内
			try:
				#load_str="delete from `stock_"+file.split('.')[0]+"` where trx_date='"+str(date)+"'"
				#cur.execute(load_str)
				#load_str="load data local infile '"+ dir + "/" +file + "' REPLACE INTO TABLE stock_"+file.split('.')[0]+" fields terminated by ',' (trx_date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20); "
				#cur.execute(load_str)
				load_str="delete from `stock_"+file.split('.')[0]+"` where trx_date='"+str(date)+"'"
				cur.execute(load_str)
				conn.commit()
			except MySQLdb.Error,e:
				#新股，表不存在时，建表
				print file+" fail "+str(e.args[0]) + str(e.args[1])
				
			print file + " success"
	cur.close()
	conn.close()

load("2016-5-3")