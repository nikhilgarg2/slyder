from .connect import *
from selenium import webdriver
import MySQLdb
import time


def get1(r,prod,proda):
    try:
        j=r.find_element_by_css_selector(prod).get_attribute(proda)
        return j
    except Exception as d:
        return "N/A"
    
def get2(r,attri):
    try:
        j=r.find_element_by_css_selector(attri).text
        return j
    except Exception as d:
        return 0


def compile2(css,prod, proda, naam, maxrp, sellp,driver,crawl,category):
    sql="SELECT * FROM `final` WHERE `crawl_id`=%s" % crawl
    cursor.execute(sql)
    trying=cursor.fetchone()
    parent=[]
    parent=driver.find_elements_by_css_selector(css)
    #print trying[0]
    sql3="SELECT * FROM `crawl_url` WHERE `id`= %s"
    valus=trying[7]
    cursor.execute(sql3,valus)
    try2=cursor.fetchone()
    for e in parent:
        p=get1(e,prod,proda)
        n=get2(e,naam)
        s=get2(e,sellp)
        m=get2(e,maxrp)
        if m==0:
            m=s
        sql1="INSERT INTO `dump_val`(`crawl_item_id`,`name`,`mrp`,`sp`,`final_id`,`crawl_date`,`reconciled`,\
             `reconciled_date`) VALUES(%s,%s,%s,%s,%s,%s,FALSE,%s)"
        values=(p,n,m,s,try2[1],time.strftime('%Y-%m-%d %H:%M:%S'),time.strftime('%Y-%m-%d %H:%M:%S'))
        cursor.execute(sql1,values)
        db.commit()
    