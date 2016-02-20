#coding:utf-8
#数据导入数据库
import MySQLdb
import os

try:
	conn=MySQLdb.connect(host="localhost",user="root",db="stock")
	cur=conn.cursor()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])	
dir = "E:\\\Project\\\Python\\\download"
for file in os.listdir(dir):
	print dir + "\\" +file
	if os.path.isfile(dir + "\\" + file):
		#载入数据库内
		try:
			load_str="load data local infile '"+ dir + "\\\\" +file + "' replace INTO TABLE STOCK.STOCK fields terminated by ',' (stock_id,trx_date,open_price,high_price,low_price,close_price,volume,adj_close_price); "
			cur.execute(load_str)
			load_str="delete from stock.stock where trx_date='0000-00-00'"
			cur.execute(load_str)
			conn.commit()
		except MySQLdb.Error,e:
			print "%d: 载入发生错误 %d: %s" % (file, e.args[0], e.args[1])
		print file + "载入数据库成功"
cur.close()
conn.close()