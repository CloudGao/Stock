#coding:utf-8
#每日数据更新总控过程
import update_stock_market,daily_update_stock_download,daily_transform_update,daily_update_stock_load
import sys

path = sys.argv[0][0:len(sys.argv[0])-13]
date = '2016-05-13'
print(path)

update_stock_market.update_market()
print ("update_stock_market")
daily_update_stock_download.download(date,date,'D')
print ("daily_update_stock_download")
daily_transform_update.transfrom()
print ("daily_transform_update")
daily_update_stock_load.load(date)
print ("daily_update_stock_load")
print ("finish")