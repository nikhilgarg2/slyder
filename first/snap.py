import time
from selenium import webdriver
import MySQLdb
import re
from .connect import *

def get_name(i):
	try:
		x=i.find_element_by_css_selector('.product-image').get_attribute('alt')
		return x
	except Exception as d:
		return "N/A"

def get_prodid(i):
	try:
		x=i.find_element_by_css_selector('.product-title a').get_attribute('pogid')
		return x
	except Exception as d:
		print d
		return "N/A"

def get_price(i):
	try:
		x=i.find_element_by_css_selector('.product-price').text		
		x=re.sub(r'[^0-9^\ ]','',x)
		#print x
		lis=[]
		len(lis)
		lis=x.split()
		if len(lis)==0:
			lis.append(0)
			lis.append(0)
			lis.append(0)
			return lis
		elif len(lis)==1:
			lis.append(lis[0])
			lis.append(lis[0])
			return lis
		elif len(lis)==2:
			lis.append(lis[0])
			return lis
		else:
			return lis

	except Exception as d:
		#print d
		lis=[]
		lis.append(0)
		lis.append(0)
		lis.append(0)
		return lis

def snap_crawl(css,prod, proda, naam, maxrp, sellp,driver,crawl,category):
	try :
		x=driver.find_element_by_xpath('//*[@id="no-of-results-filter"]').text
		x=int(x)
		x=(x/20)+1
	except Exception as d:
		x=50
	
	for i in range(0,x):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  		time.sleep(7)
        e=[]
	e=driver.find_elements_by_css_selector('.product_grid_cont')
	sql="SELECT * FROM `final` WHERE `crawl_id`=%s" % crawl
        cursor.execute(sql)
        trying=cursor.fetchone()
        sql3="SELECT * FROM `crawl_url` WHERE `id`= %s"
        valus=trying[7]
        cursor.execute(sql3,valus)
        try2=cursor.fetchone()
        
        for i in e:
		progid=get_prodid(i)
		name=get_name(i)
		price=get_price(i)
		#print price
		mrp=price[0]
		sp=price[2]
		sql1="INSERT INTO `dump_val`(`crawl_item_id`,`name`,`mrp`,`sp`,`final_id`,`crawl_date`,`reconciled`,\
                         `reconciled_date`) VALUES(%s,%s,%s,%s,%s,%s,FALSE,%s)"
		values=(progid,name,mrp,sp,try2[1],time.strftime('%Y-%m-%d %H:%M:%S'),time.strftime('%Y-%m-%d %H:%M:%S'))
		cursor.execute(sql1,values)
                db.commit()