import os
import sys
sys.path.append(os.path.abspath('../'))
import time
from selenium import webdriver
import MySQLdb
import re
from slyder.connect import *


def get_name(driver1):
    try:
        x=driver1.find_element_by_xpath('//*[@itemprop="name"]').text
        y=driver1.find_element_by_css_selector('.selected').text
        z=" ".join((x,y))
        return z
    except Exception as d:
        return "N/A"

def get_mrp(driver1):
            try:
                x=driver1.find_element_by_xpath('//*[@id="original-price-id"]').text
                if not x:
                    x=0
                return x
            except Exception as d:
                return 0

def get_sp(driver1):
        try:
            x=driver1.find_element_by_xpath('//*[@id="selling-price-id"]').text
            if not x:
                x=0
            return x
        except Exception as d:
            return 0

def get_prod(driver1):
            try:
                x=driver1.find_element_by_xpath('//*[@id="pppid"]').get_attribute('innerHTML')
                if not x:
                    x="N/A"
                return x
            except Exception as d:
                return "N/A"
    


def snap_crawl1(css,prod, proda, naam, maxrp, sellp,driver,crawl,category):
        sql="SELECT * FROM `final` WHERE `crawl_id`=%s" % (crawl)
        cursor.execute(sql)
        trying=cursor.fetchone()
        #parent=[]
        #links=[]
        #parent=driver.find_elements_by_css_selector(css)
        sql3="SELECT * FROM `crawl_url` WHERE `id`= %s"
        valus=trying[7]
        cursor.execute(sql3,valus)
        try2=cursor.fetchone()
        try:
		x=driver.find_element_by_xpath('//*[@id="no-of-results-filter"]').text
		x=int(x)
		x=(x/20)+1
	except Exception as d:
		x=50
	
	for i in range(0,x):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  		time.sleep(7)
    
        product=[]
        product=driver.find_elements_by_css_selector('.product_grid_cont')
        link=[]
        for i in product:
            x=i.find_element_by_css_selector('.product-title a').get_attribute('href')
            link.append(x)
        
        driver1=webdriver.Firefox()
        for lin in link:
            driver1.get(lin)
            clik=[]
            clik=driver1.find_elements_by_css_selector('.attrActive')
            for z in clik:
                z.click()
                time.sleep(2)
                name=get_name(driver1)
                mrp=get_mrp(driver1)
                sp=get_sp(driver1)
                prod=get_prod(driver1)
                print prod
                sql1="INSERT INTO `dump_val`(`crawl_item_id`,`name`,`mrp`,`sp`,`final_id`,`crawl_date`,`reconciled`,\
                         `reconciled_date`) VALUES(%s,%s,%s,%s,%s,%s,FALSE,%s)"
                values=(prod,name,mrp,sp,try2[0],time.strftime('%Y-%m-%d %H:%M:%S'),time.strftime('%Y-%m-%d %H:%M:%S'))
                cursor.execute(sql1,values)
                db.commit()
        driver1.close()        
