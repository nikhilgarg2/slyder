from selenium import webdriver
import MySQLdb
import time
#from .compile import compile1
from .connect import *
from .dump import compile2
from .reconcile import reconcile
from .ama_comp import compile3
from .dumpi import dump2

def scroll_first(css,prod, proda, naam, maxrp, sellp, crawl,category):
    
    sql1="SELECT * FROM `crawl_url` WHERE `id`='%s'" % crawl
    cursor.execute(sql1)
    trying=cursor.fetchone()
    #chromedriver = "/usr/bin/chromedriver"
    #driver = webdriver.Chrome(chromedriver)
    #time.time()
    driver=webdriver.Firefox()
    driver.get(trying[2])
    sql1="SELECT * FROM `scroll` WHERE `web_id`='%d'" %(int(trying[1]))
    cursor.execute(sql1)
    final=cursor.fetchone()
    #print "done"
    
    if final[1]==False:
     for i in range(100):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to bottom of page
        time.sleep(5)
     dump2(crawl)
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
                    #print e
                    continue
            except Exception as d:
                 break
        dump2(crawl)
        compile2(css,prod, proda, naam, maxrp, sellp,driver,crawl,category)
        
    driver.close()
    
    reconcile(category)
 #   item_dump()
    
    
