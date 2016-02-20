#coding:utf-8
#2015-11-30 需要添加外部控制线程，在网络超时的时候进行重试
import urllib2,socket,threading,time,random,re
#拉取代理列表
def get_proxy(file_name):
	try:
		f = open("E:\Project\Python\output.txt","r")
		proxy_list = []
		for line in f.readlines():
			temp_line = line.strip()
			pattern_type = re.compile(r'\w+')
			match_type = pattern_type.search(temp_line)
			pattern_ip = re.compile(r'\d+.\d+.\d+.\d+:\d+')
			match_ip = pattern_ip.search(temp_line)
			proxy_list.append({match_type.group():match_ip.group()})
	finally:
		f.close()
	return proxy_list
proxy_list = get_proxy("E:\\Project\\Python\\output.txt")
#从雅虎财经网站下载日线数据
#stock_exchange 字符串，股票代码抬头，上海600000，深圳000000
#counter 数字，起始股票代码
#max_stock_code 整数，该交易所最大股票代码
#stock_exchange_name 字符串，交易所缩写，上证股票是股票代码后面加上.ss，深证股票是股票代码后面加上.sz
#另外，上证综指代码：000001.ss，深证成指代码：399001.SZ，沪深300代码：000300.ss
def spider(stock_exchange,counter,stock_exchange_name,proxy,stock_list):
	#counter = 336 #下到318
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	#设置使用代理
	proxy_support = urllib2.ProxyHandler(proxy)
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	#循环抓取
	stock_code = int(stock_exchange) + counter 
	url = "http://table.finance.yahoo.com/table.csv?s=" + "%06d"%(stock_code) + stock_exchange_name
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request)  
		data = response.read()  
		response.close()
	except urllib2.HTTPError, e:
		print threading.current_thread().name+"|"+"%06d"%(stock_code)+"|"+str(e.code)
		if e.code == 504:
			return -2
		return -1
	except urllib2.URLError, e:
		#打印网络连接错误
		print threading.current_thread().name+"|"+"%06d"%(stock_code)+"|"+str(e.reason)
		return -1
	except socket.timeout as e:
		#打印超时错误，超时则等待10秒后重新连接
		print("-----socket timout:",url)
		return -1
	except Exception,e:
		print(e,url)
		stock_list.append(counter)
		#exit(-1)
		return -2
	file_name = "E:\Project\Python\download\stock_" + "%06d"%(stock_code) +".csv"
	f = open(file_name,"wb")
	f.write(data)
	f.close()
	print threading.current_thread().name+"|"+"%06d"%(stock_code)+"|"+"write in success."
	return 1
#每一步
def get_stock(stock_exchange,stock_list,stock_exchange_name,proxy_list,thread_list):
	proxy = proxy_list.pop()
	while len(stock_list)>0:
		counter=stock_list.pop()
		print threading.current_thread().name+"|loading|"+"%06d"%(int(stock_exchange) + counter)
		ret = spider(stock_exchange,counter,stock_exchange_name,proxy,stock_list)
		if ret == 0:
			pass
		if ret == 1:
			pass
		if ret == -1:
			pass
		if ret == -2:
			#出现被封，换个代理继续干
			stock_list.append(counter)
			print threading.current_thread().name+"err"
			if len(proxy_list)>0:
				proxy = proxy_list.pop()
			else:
				return
		#随机休眠，防止被封
		time.sleep(random.randint(1, 8))

#根据定义的线程数，起相应的线程
#设计线程池，失败的代理将会被抛弃
def main(max_thread_amount,code,code_str,code_amount):
	stock_list = range(code_amount)
	thread_list = []
	for thread_i in range(max_thread_amount):
		t = threading.Thread(target=get_stock, args=(code,stock_list,code_str,proxy_list,thread_list),name='sp_cy'+str(thread_i))
		t.start()

#main("300000",".sz",500)
#main("600000",".ss",2000)
main(50,"000000",".sz",289)