#coding:utf-8
#代理服务器下载及测试
import urllib2,socket,time
import re
#在http://www.xicidaili.com/网站上解析代理服务器，列举出来
def findProxies(html):
	position_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td>\n      <td>\d{1,5}</td>\n      <td>\n        <a href="\S+</a>\n      </td>\n      <td>高匿</td>\n      <td>\w+')
	position_lines = position_pattern.findall(html)
	results = []
	n = 0
	for position_line in position_lines:
		position_pattern = re.compile(r'</td>\n      <td>')
		proxytype_pattern3 = re.compile('</td>\n      <td>\n        <a href="\S+</a>\n      </td>\n      <td>高匿</td>\n      <td>')
		ip_line = proxytype_pattern3.split(position_line)
		proxydict = {ip_line[1]:position_pattern.sub(r':', ip_line[0])}
		n=n+1
		#print proxydict
		results.append(proxydict)
	print "Get " + str(n) + " IPs"
	return results
#打开列有大量代理服务器地址的网站
def openurl(url):
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request)  
		data = response.read()
		results = findProxies(data)
		response.close()
		return results
	except urllib2.URLError, e:
		#打印网络连接错误
		print e
	except socket.timeout as e:
		#打印超时错误，超时则等待10秒后重新连接
		print("-----socket timout:",url)
#测试具体的代理服务器能否使用
def testproxy(proxy):
	#设置使用代理
	proxy_support = urllib2.ProxyHandler(proxy)
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	url = "http://www.baidu.com"
	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request)  
		data = response.read()  
		response.close()
	except urllib2.URLError, e:
		#返回失败
		#print str(proxy) + "success"
		return False
	finally:
		pass
	#print str(proxy) + "ture"
	return True
#循环校验每个代理服务器是否正确
def testproxys(proxys):
	n = 0
	test_results = []
	print len(proxys)
	for proxy in proxys:
		print "Test" + str(n) + "IP" + str(proxy)
		testbool = testproxy(proxy)
		if testbool:
			test_results.append(proxy)
		n = n + 1
		print str(testbool)
	return test_results
#保存成功的代理服务器列表
def save(testedlist):
	try:
		f = open("E:\\Project\\Python\\output.txt", 'w')
	except:
		exit(-1)
	for r in testedlist:
		f.write(str(r) + '\n')
	f.close()
	print "Save!"
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#抓取
#url = "http://www.xicidaili.com/nt"
url = "http://www.xicidaili.com/nn"
results = openurl(url)
results.extend(openurl("http://www.xicidaili.com/nn/2"))
results.extend(openurl("http://www.xicidaili.com/nn/3"))
tested_results = testproxys(results)
save(tested_results)