from selenium import webdriver
import MySQLdb
import time
from .connect import *
def compile1(css,crawl_at, crawl_id, text2, prod,driver):
        
   
    sql1="SELECT * FROM `crawl_url` WHERE `id`='%d'" % (int(crawl_id))
    cursor.execute(sql1)
    result=cursor.fetchone()
    result=result[2]
    #print result
    
    sql2="SELECT * FROM `prodid` WHERE `id`='%d'" % (int(prod))
    cursor.execute(sql2)
    result1=cursor.fetchone()
    
    prodlist=[]
    prodlist=driver.find_elements_by_css_selector(result1[1])
    
    text1=[]
    text1=driver.find_elements_by_css_selector(css)
    print len(text1)
    sql3="SELECT * FROM `crawl_url_attribute_css_sel` WHERE `css_sel`='%s' " % (css)
    cursor.execute(sql3)
    number1=cursor.fetchone()
    number=number1[0]
    css2=number1[8]   
    if result1[3]==1:
        if int(text2)==1:
         for i in range(len(text1)):
            try1="INSERT INTO `crawl_url_attribute_css_sel_value`(`crawl_item_id`,`crawl_url_attribute_css_sel_id`,`value`,`reconciled`)VALUES('%s','%d','%s',FALSE) " % (prodlist[i].text, number,db.escape_string(text1[i].text))
            cursor.execute(try1)
            db.commit()
        elif int(text2)==2:                                                                                                                                                               
         for i in range(len(text1)):
            try1="INSERT INTO `crawl_url_attribute_css_sel_value`(`crawl_item_id`,`crawl_url_attribute_css_sel_id`,`value`,`reconciled`)VALUES('%s','%d','%s',FALSE) " % (prodlist[i].text, number,db.escape_string(text1[i].get_attribute('href')))
            cursor.execute(try1)
            db.commit()    
        
        else:
         for i in range(len(text1)):
            try1="INSERT INTO `crawl_url_attribute_css_sel_value`(`crawl_item_id`,`crawl_url_attribute_css_sel_id`,`value`,`reconciled`)VALUES('%s','%d','%s',FALSE) " % (prodlist[i].text, number,db.escape_string(text1[i].get_attribute(css2)))
            cursor.execute(try1)
            db.commit()
    
    
    elif result1[3]==2:
        if int(text2)==1:
         for i in range(len(text1)):
            try1="INSERT INTO `crawl_url_attribute_css_sel_value`(`crawl_item_id`,`crawl_url_attribute_css_sel_id`,`value`,`reconciled`)VALUES('%s','%d','%s',FALSE) " % (prodlist[i].get_attribute('href'), number,db.escape_string(text1[i].text))
            cursor.execute(try1)
            db.commit()
       
        
        elif int(text2)==2:
         for i in range(len(text1)):
            try1="INSERT INTO `crawl_url_attribute_css_sel_value`(`crawl_item_id`,`crawl_url_attribute_css_sel_id`,`value`,`reconciled`)VALUES('%s','%d','%s',FALSE) " % (prodlist[i].get_attribute('href'), number,db.escape_string(text1[i].get_attribute('href')))
            cursor.execute(try1)
            db.commit()
       
        
        else:
         for i in range(len(text1)):
            try1="INSERT INTO `crawl_url_attribute_css_sel_value`(`crawl_item_id`,`crawl_url_attribute_css_sel_id`,`value`,`reconciled`)VALUES('%s','%d','%s',FALSE) " % (prodlist[i].get_attribute('href'), number,db.escape_string(text1[i].get_attribute(css2)))
            cursor.execute(try1)
            db.commit() 
              
        
    else: 
        print 'hello'
        if int(text2)==1:
         print 'done1'
         for i in range(len(text1)):
            try1="INSERT INTO `crawl_url_attribute_css_sel_value`(`crawl_item_id`,`crawl_url_attribute_css_sel_id`,`value`,`reconciled`)\
                 VALUES(%s, %s, %s,FALSE) "
            values=(prodlist[i].get_attribute(result1[4]), int(number), text1[i].text)
           
            cursor.execute(try1,values)
            db.commit()
           # print 'exiting'
        
        elif int(text2)==2:
         for i in range(len(text1)):
            try1="INSERT INTO `crawl_url_attribute_css_sel_value`(`crawl_item_id`,`crawl_url_attribute_css_sel_id`,`value`,`reconciled`)VALUES('%s','%d','%s',FALSE) " % (prodlist[i].get_attribute(result1[4]), number,db.escape_string(text1[i].get_attribute('href')))
            cursor.execute(try1)
            db.commit()
        
        else:
         for i in range(len(text1)):
            try1="INSERT INTO `crawl_url_attribute_css_sel_value`(`crawl_item_id`,`crawl_url_attribute_css_sel_id`,`value`,`reconciled`)VALUES('%s','%d','%s',FALSE) " % (prodlist[i].get_attribute(result1[4]), number,db.escape_string(text1[i].get_attribute(css2)))
            cursor.execute(try1)
            db.commit()
    
    print 'exiting'