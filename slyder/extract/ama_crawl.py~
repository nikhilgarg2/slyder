import os
import sys
sys.path.append(os.path.abspath('../'))
from selenium import webdriver
import MySQLdb
import time
from slyder.connect import *
from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponseRedirect

def get1(r,prod,proda):
    try:
        j=r.get_attribute('name')
        return j
    except Exception as d:
        return "N/A"
    
def get2(r,attri):
    try:
        j=r.find_element_by_css_selector(attri).text
        return j
    except Exception as d:
        return 0


def compile3(css,prod, proda, naam, maxrp, sellp,driver,crawl,category):
    sql="SELECT * FROM `final` WHERE `crawl_id`=%s" % (crawl)
    cursor.execute(sql)
    trying=cursor.fetchone()
    parent=[]
    links=[]
    parent=driver.find_elements_by_css_selector(css)
    sql3="SELECT * FROM `crawl_url` WHERE `id`= %s"
    valus=trying[7]
    cursor.execute(sql3,valus)
    try2=cursor.fetchone()
    for e in parent:
        try:
             x=e.find_element_by_css_selector('div.seeMoreVariations')
             y=x.find_element_by_css_selector('a')
             links.append(y)
        except Exception as d:
            p=get1(e,prod,proda)
            n=get2(e,naam)
            s=get2(e,sellp)
            m=get2(e,maxrp)
            if m==0:
               m=s
            if not p:
                p="N/A"
            sql1="INSERT INTO `dump_val`(`crawl_item_id`,`name`,`mrp`,`sp`,`final_id`,`crawl_date`,`reconciled`,\
                         `reconciled_date`) VALUES(%s,%s,%s,%s,%s,%s,FALSE,%s)"
            values=(p,n,m,s,try2[0],time.strftime('%Y-%m-%d %H:%M:%S'),time.strftime('%Y-%m-%d %H:%M:%S'))
            cursor.execute(sql1,values)
            db.commit()
    
    print "not empty"
    driver1=webdriver.Firefox()
    for z in links:
        lk=z.get_attribute('href')
        driver1.get(lk)
        e=driver1.find_elements_by_xpath('//*[@data-feature-name="twister"]')
        #print len(e)
        x=e[0]
        e=x.find_elements_by_css_selector('ul.a-button-list')


        if len(e)==2:
            q=e[0].find_elements_by_css_selector('button.a-button-text')
            for z in q:
                 z.click()
                 time.sleep(5)
                 i=e[1]
                 p="N/A"
                 naam=".a-size-large"
                 sp=".a-color-price"
                 mrp=".a-text-strike"
                 n=get2(driver1,naam)
                 s=get2(driver1,sp)
                 m=get2(driver1,mrp)
                 if m==0:
                       m=s
                 sql1="INSERT INTO `dump_val`(`crawl_item_id`,`name`,`mrp`,`sp`,`final_id`,`crawl_date`,`reconciled`,\
                         `reconciled_date`) VALUES(%s,%s,%s,%s,%s,%s,FALSE,%s)"
                 values=(p,n,m,s,try2[0],time.strftime('%Y-%m-%d %H:%M:%S'),time.strftime('%Y-%m-%d %H:%M:%S'))
                 cursor.execute(sql1,values)
                 db.commit()
                 r=[]
                 r=i.find_elements_by_css_selector('li.swatchAvailable')
                 for g in r:
                    g.find_element_by_css_selector('button.a-button-text').click()
                    time.sleep(5)
                    p="N/A"
                    naam=".a-size-large"
                    sp=".a-color-price"
                    mrp=".a-text-strike"
                    n=get2(driver1,naam)
                    s=get2(driver1,sp)
                    m=get2(driver1,mrp)
                    if m==0:
                       m=s
                    sql1="INSERT INTO `dump_val`(`crawl_item_id`,`name`,`mrp`,`sp`,`final_id`,`crawl_date`,`reconciled`,\
                         `reconciled_date`) VALUES(%s,%s,%s,%s,%s,%s,FALSE,%s)"
                    values=(p,n,m,s,try2[0],time.strftime('%Y-%m-%d %H:%M:%S'),time.strftime('%Y-%m-%d %H:%M:%S'))
                    cursor.execute(sql1,values)
                    db.commit()
                               
                    #print driver1.find_element_by_css_selector('span.a-size-large').text

        elif len(e)==1:
  
              p="N/A"
              naam=".a-size-large"
              sp=".a-color-price"
              mrp=".a-text-strike"
              n=get2(driver1,naam)
              s=get2(driver1,sp)
              m=get2(driver1,mrp)
              if m==0:
                       m=s
              sql1="INSERT INTO `dump_val`(`crawl_item_id`,`name`,`mrp`,`sp`,`final_id`,`crawl_date`,`reconciled`,\
                         `reconciled_date`) VALUES(%s,%s,%s,%s,%s,%s,FALSE,%s)"
              values=(p,n,m,s,try2[0],time.strftime('%Y-%m-%d %H:%M:%S'),time.strftime('%Y-%m-%d %H:%M:%S'))
              cursor.execute(sql1,values)
              db.commit()
              r=[]
              i=e[0]        
              r=i.find_elements_by_css_selector('li.swatchAvailable')
              for g in r:
                g.find_element_by_css_selector('button.a-button-text').click()
                time.sleep(5)
                p="N/A"
                naam=".a-size-large"
                sp=".a-color-price"
                mrp=".a-text-strike"
                n=get2(driver1,naam)
                s=get2(driver1,sp)
                m=get2(driver1,mrp)
                if m==0:
                    m=s
                sql1="INSERT INTO `dump_val`(`crawl_item_id`,`name`,`mrp`,`sp`,`final_id`,`crawl_date`,`reconciled`,\
                        `reconciled_date`) VALUES(%s,%s,%s,%s,%s,%s,FALSE,%s)"
                values=(p,n,m,s,try2[0],time.strftime('%Y-%m-%d %H:%M:%S'),time.strftime('%Y-%m-%d %H:%M:%S'))
                cursor.execute(sql1,values)
                db.commit()            
    driver1.close()    


