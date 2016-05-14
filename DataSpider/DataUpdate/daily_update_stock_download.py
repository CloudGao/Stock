#coding:utf-8
#2016-4-29 日线数据下载
#更改数据源 从tushare的源下载包含MA5等均线
import urllib2,socket,threading,time,random,re,MySQLdb
import tushare 

#每一步
def get_stock(stock_list,start,end,type):
	while len(stock_list)>0:
		stock_code=stock_list.pop()
		df = tushare.get_hist_data(code=stock_code,start=start,end=end,ktype=type)
		if(type == 'D'):
			stock_code = 'D_'+stock_code
		elif(type == 'W'):
			stock_code = 'W_'+stock_code
		elif(type == 'M'):
			stock_code = 'M_'+stock_code
		elif(type == '5'):
			stock_code = '5_'+stock_code
		elif(type == '15'):
			stock_code = '15_'+stock_code
		elif(type == '30'):
			stock_code = '30_'+stock_code
		elif(type == '60'):
			stock_code = '60_'+stock_code
		df.to_csv('E:/Project/Python/STOCK/DataSpider/DataUpdate/daily_update_d_download2/'+stock_code+'.csv')
		print("save "+stock_code)

#根据定义的线程数，起相应的线程
#设计线程池，失败的代理将会被抛弃
def download(start,end,type):
	try:
		conn=MySQLdb.connect(host="localhost",user="root",db="stock_1.0")
		cur=conn.cursor()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])	

	#先生成所有股票列表
	#可以从昨天的大盘指数列表中得到股票列表，停牌的涨跌幅为0，所以无所谓
	try:
		load_str="SELECT `code` FROM current_market order by code asc"
		cur.execute(load_str)
		result = cur.fetchall()
		stock_list = []
		for code in result:
			stock_list.append(code[0])
	except MySQLdb.Error,e:
		#数据库读取错误
		print file+" fail "+str(e.args[0]) + str(e.args[1])
		return
	finally:
		cur.close()
		conn.close()
	stock_list_temp = stock_list
	#下数据
	#for thread_i in range(max_thread_amount):
	#	t = threading.Thread(target=get_stock, args=(stock_list_temp,start,end,type),name="Thread")
	#	t.start()
	get_stock(stock_list_temp,start,end,type)
		

