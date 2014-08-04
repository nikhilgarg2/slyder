import os
import sys
sys.path.append(os.path.abspath('../..'))
from selenium import webdriver
import MySQLdb
import time
#from .compile import compile1
from slyder.settings.connect import *
from slyder.extract.crawl_gen import compile2
from slyder.reconcile.reconcile import reconcile
from slyder.extract.ama_crawl import compile3
from slyder.reconcile.dumpi import dump2
from slyder.extract.snap_crawl import snap_crawl1


def scroll_first(css,prod, proda, naam, maxrp, sellp, crawl,category):
    
    sql1="SELECT * FROM `crawl_url` WHERE `id`=%s"
    value=crawl
    cursor.execute(sql1,value)
    trying=cursor.fetchone()
    driver=webdriver.Firefox()
    driver.get(trying[2])
    time.sleep(5)
    sql1="SELECT * FROM `scroll` WHERE `web_id`=%s"
    value1=(trying[1])
    cursor.execute(sql1,value1)
    final=cursor.fetchone()
    #print trying[1]
    #print final
    if final[1]==False:
     dump2(crawl)
     quer="SELECT `address` FROM `website` WHERE `id`=%s"
     vai=(final[4])
     cursor.execute(quer,vai)
     name=cursor.fetchone()
     if "snapdeal" in name[0]:
        print "done"
        snap_crawl1(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)
     else:
        for i in range(100):
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to bottom of page
          time.sleep(5)
        compile2(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)      
    
    elif final[1] == True and final[3]==True:
     quer="SELECT `address` FROM `website` WHERE `id`=%s"
     vai=(final[4])
     cursor.execute(quer,vai)
     name=cursor.fetchone()
     dump2(crawl)
     while True:
      try:
        driver.find_element_by_xpath(final[2])  #
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            if 'amazon' in name[0]:
                compile3(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)
            else:
                compile2(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)
            time.sleep(5)
            if driver.find_element_by_xpath(final[2]).is_enabled():
             driver.find_element_by_xpath(final[2]).click()
            time.sleep(5)
        except Exception as e:
            if 'amazon' in name[0]:
                compile3(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)
            else:
                compile2(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)
            continue
      except Exception as d:
        if 'amazon' in name[0]:
                compile3(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)
        else:
                compile2(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)
        break
     
    
    elif final[1]==True and final[3]==False:
        while True:
            time.sleep(8)
            try: 
                driver.find_element_by_xpath(final[2])  #
                try:
                    
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(5)
                    if driver.find_element_by_xpath(final[2]).is_enabled():
                      driver.find_element_by_xpath(final[2]).click()
                    
                except Exception as e:
                    
                    continue
            except Exception as d:
                 break
        
        dump2(crawl)
        
        compile2(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)
        
    driver.close()
    
    reconcile(category)
 #   item_dump()
    
    
