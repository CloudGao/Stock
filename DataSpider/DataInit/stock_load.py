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
	dir = "E:/Project/Python/STOCK/DataSpider/DataInit/download"
	for file in os.listdir(dir):
		print dir + "/" +file
		if os.path.isfile(dir + "/" + file):
			#载入数据库内
			try:
				load_str="delete from `stock_"+file.split('.')[0]+"` where trx_date='"+str(date)+"'"
				cur.execute(load_str)
				load_str="load data local infile '"+ dir + "/" +file + "' REPLACE INTO TABLE stock_"+file.split('.')[0]+" fields terminated by ',' (trx_date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover); "
				cur.execute(load_str)
				conn.commit()
			except MySQLdb.Error,e:
				#新股，表不存在时，建表
				print file+" fail "+str(e.args[0]) + str(e.args[1])
				if(e.args[0] == 1146):
					load_str="CREATE TABLE `stock_"+file.split('.')[0]+"` ( `id` int auto_increment, `trx_date` date DEFAULT NULL unique,  `open` float DEFAULT NULL,  `high` float DEFAULT NULL,  `close` float DEFAULT NULL,  `low` float DEFAULT NULL,  `volume` float DEFAULT NULL,  `price_change` float DEFAULT NULL,  `p_change` float DEFAULT NULL,  `ma5` float DEFAULT NULL,  `ma10` float DEFAULT NULL,  `ma20` float DEFAULT NULL,  `v_ma5` float DEFAULT NULL,  `v_ma10` float DEFAULT NULL,  `v_ma20` float DEFAULT NULL,  `turnover` double DEFAULT NULL ,primary key(id),KEY `main` (`trx_date`) USING BTREE) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
					cur.execute(load_str)
					load_str="load data local infile '"+ dir + "/" +file + "' replace INTO TABLE stock_"+file.split('.')[0]+" fields terminated by ',' (trx_date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover); "
					cur.execute(load_str)
					load_str="delete from `stock_"+file.split('.')[0]+"` where trx_date='0000-00-00'"
					cur.execute(load_str)
					conn.commit()
				print file+"build "
			print file + " success"
	cur.close()
	conn.close()

